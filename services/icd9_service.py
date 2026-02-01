from __future__ import annotations

import re
from typing import Any, Dict, List, Optional

import pandas as pd

class ICD9LookupService:
    def __init__(self, csv_path: str):
        self.csv_path = csv_path

        self.all_codes: List[str] = []
        self.code_to_long: Dict[str, str] = {}
        self.code_to_short: Dict[str, str] = {}

    def load(self) -> None:
        dx = pd.read_csv(self.csv_path, dtype=str)

        required = {"dgns_cd", "longdesc", "shortdesc"}
        missing = required - set(dx.columns)
        if missing:
            raise RuntimeError(f"Faltan columnas en CSV: {missing}. Columnas actuales: {list(dx.columns)}")

        self.all_codes = dx["dgns_cd"].astype(str).tolist()
        self.code_to_long = dict(zip(dx["dgns_cd"], dx["longdesc"]))
        self.code_to_short = dict(zip(dx["dgns_cd"], dx["shortdesc"]))

    @staticmethod
    def decimalize(code: str) -> str:
        s = str(code).strip()
        if not s.isdigit():
            return s
        if len(s) <= 3:
            return s.zfill(3)
        return s[:3] + "." + s[3:]

    def lookup_icd9_smart(self, code_raw: str, max_children: int = 10) -> Dict[str, Any]:
        code_raw = str(code_raw).strip()

        if not re.fullmatch(r"\d{3,6}", code_raw):
            return {"query": code_raw, "found": False, "reason": "non-numeric"}

        if code_raw in self.code_to_long:
            return {
                "query": code_raw,
                "found": True,
                "code_csv": code_raw,
                "code_decimal": self.decimalize(code_raw),
                "longdesc": self.code_to_long[code_raw],
                "shortdesc": self.code_to_short.get(code_raw),
                "note": "exact match",
            }

        if len(code_raw) == 4:
            children = [c for c in self.all_codes if c.startswith(code_raw) and len(c) >= 5]
            children = sorted(children)[:max_children]

            padded0 = code_raw + "0"
            best_guess: Optional[Dict[str, Any]] = None
            if padded0 in self.code_to_long:
                best_guess = {
                    "code_csv": padded0,
                    "code_decimal": self.decimalize(padded0),
                    "longdesc": self.code_to_long[padded0],
                    "shortdesc": self.code_to_short.get(padded0),
                    "note": "best_guess: padded 0 (often NOS)",
                }

            if children:
                return {
                    "query": code_raw,
                    "found": False,
                    "reason": "no exact; returning child candidates",
                    "query_decimal": self.decimalize(code_raw),
                    "best_guess": best_guess,
                    "children": [
                        {
                            "code_csv": c,
                            "code_decimal": self.decimalize(c),
                            "longdesc": self.code_to_long.get(c),
                            "shortdesc": self.code_to_short.get(c),
                        }
                        for c in children
                    ],
                }

            if padded0 in self.code_to_long:
                return {
                    "query": code_raw,
                    "found": True,
                    "code_csv": padded0,
                    "code_decimal": self.decimalize(padded0),
                    "longdesc": self.code_to_long[padded0],
                    "shortdesc": self.code_to_short.get(padded0),
                    "note": "matched by padding 0 (no children found)",
                }

        return {"query": code_raw, "found": False, "reason": "no match"}