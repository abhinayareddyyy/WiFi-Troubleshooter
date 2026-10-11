from __future__ import annotations

from typing import Any

from backend.diagnostics.connectivity import check_external_connectivity, check_gateway
from backend.diagnostics.dns_check import check_dns_resolution
from backend.diagnostics.latency import measure_latency
from backend.diagnostics.stability import measure_stability


def run_diagnostic(target: str = "google.com") -> dict[str, Any]:
    gateway = check_gateway()
    internet = check_external_connectivity()
    dns = check_dns_resolution(target)
    latency = measure_latency("8.8.8.8", attempts=5)
    stability = measure_stability("8.8.8.8", attempts=5)

    recommendations: list[str] = []
    if not gateway["reachable"]:
        recommendations.append("Check whether the default gateway is reachable and confirm the router is online.")
    if not internet["reachable"]:
        recommendations.append("Test internet access with another target or verify the ISP link and firewall rules.")
    if not dns["reachable"]:
        recommendations.append("Verify the DNS server settings or test connectivity with a direct IP before troubleshooting the resolver.")
    if latency["average_ms"] is not None and latency["average_ms"] > 200:
        recommendations.append("High latency suggests congestion, interference, or routing issues; try moving closer to the access point.")
    if not recommendations:
        recommendations.append("Network conditions appear healthy. Continue monitoring for intermittent instability.")

    summary = (
        "Connectivity is healthy." if gateway["reachable"] and internet["reachable"] and dns["reachable"] else
        "Some network checks are failing and should be investigated."
    )

    return {
        "gateway": gateway,
        "internet": internet,
        "dns": dns,
        "latency": latency,
        "stability": stability,
        "summary": summary,
        "recommendations": recommendations,
    }
