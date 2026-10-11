from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.database import get_recent_diagnostics, save_diagnostic
from backend.models import DiagnoseRequest
from backend.services.diagnosis import run_diagnostic

app = FastAPI(title="NetPulse", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "netpulse"}


@app.post("/api/diagnose")
def diagnose(request: DiagnoseRequest) -> dict:
    result = run_diagnostic(request.target)
    save_diagnostic(result)
    return result


@app.get("/api/demo")
def demo_diagnostic() -> dict:
    return run_diagnostic("google.com")


@app.get("/api/history")
def diagnostic_history() -> dict[str, list[dict]]:
    return {"items": get_recent_diagnostics(limit=10)}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("backend.main:app", host="127.0.0.1", port=8000, reload=True)
