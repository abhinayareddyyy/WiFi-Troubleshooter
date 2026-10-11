from __future__ import annotations

import platform
import re
import socket
import subprocess
import time
from typing import Any


def detect_default_gateway() -> str:
    try:
        if platform.system() == "Windows":
            result = subprocess.run(["ipconfig"], capture_output=True, text=True, check=False)
            lines = result.stdout.splitlines()
            for index, line in enumerate(lines):
                if "Default Gateway" in line:
                    for candidate in lines[index + 1 : index + 4]:
                        match = re.search(r"\d+\.\d+\.\d+\.\d+", candidate)
                        if match:
                            return match.group(0)
            return "192.168.1.1"

        result = subprocess.run(["ip", "route"], capture_output=True, text=True, check=False)
        for line in result.stdout.splitlines():
            if line.startswith("default"):
                parts = line.split()
                if len(parts) >= 3:
                    return parts[2]
        return "192.168.1.1"
    except Exception:
        return "192.168.1.1"


def check_target(host: str, port: int = 53, timeout: float = 2.0) -> dict[str, Any]:
    start = time.perf_counter()
    try:
        with socket.create_connection((host, port), timeout=timeout):
            elapsed_ms = (time.perf_counter() - start) * 1000
            return {
                "host": host,
                "port": port,
                "reachable": True,
                "latency_ms": round(elapsed_ms, 2),
                "status": "online",
                "details": f"Connection to {host}:{port} succeeded.",
            }
    except (OSError, socket.timeout) as exc:
        elapsed_ms = (time.perf_counter() - start) * 1000
        return {
            "host": host,
            "port": port,
            "reachable": False,
            "latency_ms": round(elapsed_ms, 2),
            "status": "offline",
            "details": f"Connection to {host}:{port} failed: {exc}",
        }


def check_gateway() -> dict[str, Any]:
    gateway = detect_default_gateway()
    return check_target(gateway, port=80, timeout=2.5)


def check_external_connectivity(host: str = "8.8.8.8", port: int = 53) -> dict[str, Any]:
    return check_target(host, port=port, timeout=3.0)
