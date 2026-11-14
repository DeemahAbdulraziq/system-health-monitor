# Real-Time IT Infrastructure & Network Health Monitor

A lightweight, web-based monitoring dashboard built with Python, Flask, and psutil to track system resources and network service availability.
## Key Features
* **Real-Time Hardware Telemetry:** Continuously monitors CPU load, Memory (RAM) utilization, and Disk storage capacity with auto-refreshing metrics every 5 seconds.
* **Network & Service Health Checks:** Performs automated TCP socket connection checks against critical external nodes and ports.
* **Automated Incident Logging:** Automatically logs unreachable services or downtime events with timestamps into `network_alerts.log`.
## Tech Stack
* **Backend:** Python 3, Flask, psutil, socket, logging
* **Frontend:** HTML5, CSS3, Vanilla JavaScript (Fetch API)

## How to Run Locally
1. Clone the repository and navigate to the project folder.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
3. python app.py
4. Open your browser at http://127.0.0.1:5000