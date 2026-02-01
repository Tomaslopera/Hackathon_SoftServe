from __future__ import annotations

from fastapi import FastAPI

from schemas import PredictRequest, PredictResponseItem, HealthResponse
from services.model_service import ICD9ModelService
from services.icd9_service import ICD9LookupService


MODEL_ID = "DATEXIS/CORe-clinical-diagnosis-prediction"
CSV_PATH = "./dataset/icd9dx2015.csv"

app = FastAPI(title="ICD9 Diagnosis Prediction API", version="1.0.0")

model_service = ICD9ModelService(model_id=MODEL_ID, max_length=512)
lookup_service = ICD9LookupService(csv_path=CSV_PATH)


@app.on_event("startup")
def startup() -> None:
    model_service.load()
    lookup_service.load()


@app.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(
        status="ok",
        model=MODEL_ID,
        device=str(model_service.device),
        codes_loaded=len(lookup_service.all_codes),
    )


@app.post("/predict", response_model=list[PredictResponseItem])
def predict(req: PredictRequest) -> list[PredictResponseItem]:
    preds = model_service.predict_codes_topk(
        text=req.text,
        top_n=req.top_n,
        threshold=req.threshold,
        oversample_k=250,
    )

    enriched = model_service.enrich_predictions(
        preds=preds,
        lookup_service=lookup_service,
        include_children=req.include_children,
        max_children=req.max_children,
    )

    return enriched