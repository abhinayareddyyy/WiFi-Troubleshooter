from __future__ import annotations

import time
from typing import Any

from backend.diagnostics.connectivity import check_target


def measure_stability(host: str = "8.8.8.8", attempts: int = 5, interval_seconds: float = 0.5) -> dict[str, Any]:
    history: list[dict[str, Any]] = []
    for index in range(1, attempts + 1):
        result = check_target(host, port=53, timeout=2.0)
        history.append({"attempt": index, "reachable": result["reachable"], "latency_ms": result["latency_ms"]})
        time.sleep(interval_seconds)

    success_count = sum(1 for item in history if item["reachable"])
    failed_count = len(history) - success_count
    status = "stable" if failed_count == 0 else "intermittent"

    return {
        "target": host,
        "attempts": attempts,
        "successful_checks": success_count,
        "failed_checks": failed_count,
        "history": history,
        "status": status,
    }
