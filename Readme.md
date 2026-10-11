# NetPulse : Wi-Fi Troubleshooter & Network Health Monitor

NetPulse is a network diagnostics application designed to help users identify, understand, and troubleshoot common Wi-Fi and internet connectivity problems. It checks network connectivity, measures latency, tests DNS resolution, monitors connection stability, and provides evidence-based troubleshooting recommendations through a user-friendly dashboard.

The project is built using Python and modern web technologies, applying fundamental Computer Networks concepts to a practical, real-world problem.

## Problem Statement

When a Wi-Fi connection becomes slow or stops working, users often struggle to identify the cause. The issue could involve the local router, DNS resolution, internet connectivity, or an unreliable connection.

NetPulse aims to simplify network troubleshooting by running diagnostic checks, recording results, identifying possible failure patterns, and suggesting actionable next steps.

## Features

### 1. Connectivity Diagnostics
- Check connectivity to the default gateway.
- Test external internet reachability.
- Distinguish local gateway failures from possible external connectivity problems.
- Display clear diagnostic results.

### 2. Latency Monitoring
- Measure network response times.
- Track average and maximum observed latency.
- Visualize response-time changes over time.
- Highlight unusually high latency based on configurable thresholds.

### 3. DNS Diagnostics
- Test domain-name resolution.
- Identify potential DNS resolution failures.
- Compare DNS results with other connectivity checks to narrow down possible causes.

### 4. Connection Stability Monitoring
- Perform repeated connectivity checks.
- Record detected outages and recovery times.
- Track successful and failed checks.
- Identify intermittent connectivity problems.

### 5. Explainable Troubleshooting
- Present diagnostic findings in understandable language.
- Explain which checks failed and which succeeded.
- Suggest troubleshooting steps based on observed evidence.
- Avoid presenting uncertain diagnoses as confirmed causes.

### 6. Dashboard and Reports
- Display current diagnostic status.
- Visualize latency and connectivity history.
- Store previous diagnostic results.
- Export diagnostic reports as CSV files.

## Technology Stack

| Component | Technology |
|---|---|
| Programming language | Python |
| Backend API | FastAPI |
| Frontend | React and TypeScript |
| Styling | Tailwind CSS |
| Database | SQLite |
| Data visualization | Recharts |
| Testing | pytest |
| Version control | Git and GitHub |

## Architecture

The application consists of four main components:

1. **Frontend dashboard:** Displays diagnostic results, charts, history, and troubleshooting suggestions.
2. **Backend API:** Receives diagnostic requests and returns structured results.
3. **Diagnostic engine:** Runs connectivity, DNS, latency, and stability checks.
4. **Database:** Stores measurements, diagnostic events, and historical results.

Network diagnostics should execute on the user's computer or through a local diagnostic agent. A remote web server cannot directly test the user's private Wi-Fi network.

## Project Structure

```text
netpulse/
├── backend/
│   ├── main.py
│   ├── diagnostics/
│   │   ├── connectivity.py
│   │   ├── dns_check.py
│   │   ├── latency.py
│   │   └── stability.py
│   ├── services/
│   │   └── diagnosis.py
│   ├── database.py
│   └── models.py
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   └── services/
│   └── package.json
├── tests/
├── requirements.txt
├── .gitignore
└── README.md
```

*This structure represents the planned architecture; update it to match the actual repository as implementation progresses.*

## Installation and Setup

### Prerequisites

- Python 3.11 or later
- Node.js and npm
- Git
- A computer connected to a network

### 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd netpulse
```

Replace the placeholder with your repository URL.

### 2. Set Up the Backend

Create and activate a virtual environment.

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the Python dependencies:

```bash
pip install -r requirements.txt
```

Start the API after implementing the backend entry point:

```bash
uvicorn backend.main:app --reload
```

The API documentation should be available at:

```text
http://127.0.0.1:8000/docs
```

### 3. Set Up the Frontend

```bash
cd frontend
npm install
npm run dev
```

Open the local development URL printed by Vite in your terminal.

## How It Works

1. The diagnostic engine identifies the default gateway and performs connectivity checks.
2. It tests external reachability using configured targets.
3. It measures DNS resolution and network response times.
4. Repeated checks record changes in connectivity.
5. The diagnosis service compares the results and generates possible explanations.
6. The dashboard presents findings, historical measurements, and recommended next steps.

## Diagnostic Examples

| Observation | Possible interpretation |
|---|---|
| Gateway is unreachable | Local network, gateway, or device configuration issue |
| Gateway responds but external targets fail | Possible internet, routing, firewall, or target availability issue |
| DNS resolution fails while direct-IP connectivity succeeds | Possible DNS configuration or resolver issue |
| Latency varies significantly | Possible congestion, interference, routing variation, or target instability |
| Connectivity repeatedly drops | Possible intermittent network or device problem |

These observations help narrow down causes but do not independently prove the root cause. ICMP traffic may be blocked, and a single external target may itself be unavailable.

## Testing

Run backend tests using:

```bash
pytest
```

Tests should cover:
- Successful and failed connectivity checks.
- DNS resolution errors and timeouts.
- High latency and fluctuating response times.
- Repeated connection failures and recovery.
- Diagnostic recommendations for different combinations of results.

Use mocked network responses for repeatable automated tests. Test real connectivity separately in a controlled environment.

## Computer Networks Concepts Demonstrated

- IPv4 addressing and default gateways
- TCP/IP networking
- ICMP and connectivity testing
- DNS resolution
- Latency and timeouts
- Network availability and reliability
- Client-server architecture
- Network troubleshooting

## Security and Responsible Use

- Run diagnostics only on devices and networks you are authorized to test.
- Apply timeouts to network operations.
- Avoid collecting packet contents or personal browsing information.
- Validate diagnostic targets and limit resource usage.
- Do not expose the diagnostic API publicly without authentication and appropriate access controls.

## Future Enhancements

- Wi-Fi signal strength and interface information where supported by the operating system.
- Notifications for prolonged outages.
- Comparison of multiple external connectivity targets.
- Downloadable PDF diagnostic reports.
- A local agent for remote dashboard access.
- More advanced root-cause analysis based on historical evidence.

## Conclusion

NetPulse transforms basic network diagnostic commands into an accessible troubleshooting tool. By combining connectivity testing, DNS diagnostics, latency monitoring, historical analysis, and explainable recommendations, the project demonstrates how Computer Networks concepts can be applied to everyday internet connectivity problems.

The long-term goal is to help users move beyond knowing that their internet is not working and toward understanding which part of the connection may be failing.