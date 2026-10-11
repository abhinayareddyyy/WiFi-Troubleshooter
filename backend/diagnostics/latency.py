from __future__ import annotations

from typing import Any

from backend.diagnostics.connectivity import check_target


def measure_latency(host: str = "8.8.8.8", port: int = 443, attempts: int = 5) -> dict[str, Any]:
    samples: list[float] = []
    results: list[dict[str, Any]] = []

    for attempt in range(1, attempts + 1):
        result = check_target(host, port=port, timeout=1.5)
        results.append({"attempt": attempt, **result})
        if result["reachable"]:
            samples.append(float(result["latency_ms"] or 0))

    average_ms = round(sum(samples) / len(samples), 2) if samples else None
    max_ms = round(max(samples), 2) if samples else None
    min_ms = round(min(samples), 2) if samples else None

    return {
        "target": host,
        "port": port,
        "attempts": attempts,
        "samples": samples,
        "average_ms": average_ms,
        "max_ms": max_ms,
        "min_ms": min_ms,
        "results": results,
        "status": "healthy" if average_ms is not None and average_ms < 200 else "elevated",
    }
