from __future__ import annotations

import re
from typing import Any, Dict, List

import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

from services.icd9_service import ICD9LookupService


class ICD9ModelService:
    def __init__(self, model_id: str, max_length: int = 512):
        self.model_id = model_id
        self.max_length = max_length

        self.tokenizer = None
        self.model = None
        self.device = None

    def load(self) -> None:
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_id)
        self.model = AutoModelForSequenceClassification.from_pretrained(self.model_id)
        self.model.to(self.device)
        self.model.eval()

    @staticmethod
    def is_numeric_icd9_label(label: str) -> bool:
        # el modelo puede tener labels no numéricas (palabras)
        return bool(re.fullmatch(r"\d{3,6}", str(label)))

    @staticmethod
    def decimalize(code: str) -> str:
        s = str(code).strip()
        if not s.isdigit():
            return s
        if len(s) <= 3:
            return s.zfill(3)
        return s[:3] + "." + s[3:]

    def predict_codes_topk(
        self,
        text: str,
        top_n: int,
        threshold: float,
        oversample_k: int = 250,
    ) -> List[Dict[str, Any]]:
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True, max_length=self.max_length)
        inputs = {k: v.to(self.device) for k, v in inputs.items()}

        with torch.no_grad():
            probs = torch.sigmoid(self.model(**inputs).logits).squeeze(0)

        k = min(oversample_k, probs.numel())
        top_p, top_i = torch.topk(probs, k)

        out: List[Dict[str, Any]] = []
        for p, i in zip(top_p.tolist(), top_i.tolist()):
            label = self.model.config.id2label[i]
            if not self.is_numeric_icd9_label(label):
                continue
            if p < threshold:
                continue

            code_raw = str(label)
            out.append({
                "code_raw": code_raw,
                "code_decimal": self.decimalize(code_raw),
                "score": float(p),
            })
            if len(out) >= top_n:
                break

        return out

    def enrich_predictions(
        self,
        preds: List[Dict[str, Any]],
        lookup_service: ICD9LookupService,
        include_children: bool,
        max_children: int,
    ) -> List[Dict[str, Any]]:
        enriched = []
        for pr in preds:
            code_raw = pr["code_raw"]
            info = lookup_service.lookup_icd9_smart(code_raw, max_children=max_children)

            if not include_children and (not info.get("found", False)):
                slim = {k: info.get(k) for k in ["query", "query_decimal", "found", "reason", "best_guess"]}
                info = slim

            enriched.append({**pr, "lookup": info})
        return enriched