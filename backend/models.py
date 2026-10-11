from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class DiagnoseRequest(BaseModel):
    target: str = Field(default="google.com", description="Target hostname to diagnose")


class CheckResult(BaseModel):
    host: str
    reachable: bool
    latency_ms: float | None = None
    status: str
    details: str
    port: int | None = None


class DiagnosticResponse(BaseModel):
    gateway: dict[str, Any]
    internet: dict[str, Any]
    dns: dict[str, Any]
    latency: dict[str, Any]
    stability: dict[str, Any]
    summary: str
    recommendations: list[str]
