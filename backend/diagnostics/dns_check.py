from __future__ import annotations

import socket
from typing import Any


def check_dns_resolution(hostname: str = "google.com") -> dict[str, Any]:
    try:
        results = socket.getaddrinfo(hostname, None)
        addresses = sorted({entry[4][0] for entry in results if entry[4]})
        return {
            "hostname": hostname,
            "reachable": True,
            "resolved_ips": addresses,
            "status": "resolved",
            "details": f"DNS resolved {hostname} to {', '.join(addresses) if addresses else 'unknown addresses'}.",
        }
    except socket.gaierror as exc:
        return {
            "hostname": hostname,
            "reachable": False,
            "resolved_ips": [],
            "status": "dns_failed",
            "details": f"DNS resolution failed for {hostname}: {exc}",
        }
