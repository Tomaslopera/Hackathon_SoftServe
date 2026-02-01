from __future__ import annotations

from typing import Any, Dict, List
from pydantic import BaseModel, Field


class PredictRequest(BaseModel):
    text: str = Field(..., min_length=1)
    top_n: int = Field(3, ge=1, le=50)
    threshold: float = Field(0.30, ge=0.0, le=1.0)
    include_children: bool = Field(True)
    max_children: int = Field(3, ge=1, le=25)


class PredictResponseItem(BaseModel):
    code_raw: str
    code_decimal: str
    score: float
    lookup: Dict[str, Any]


class HealthResponse(BaseModel):
    status: str
    model: str
    device: str
    codes_loaded: int