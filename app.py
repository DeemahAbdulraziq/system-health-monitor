from datetime import datetime
import logging
import socket
from flask import Flask, jsonify, render_template
import psutil

app = Flask(__name__)

logging.basicConfig(
    filename="network_alerts.log",
    level=logging.WARNING,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

TARGETS = [
    {"name": "Google DNS", "host": "8.8.8.8", "port": 53},
    {"name": "Cloudflare DNS", "host": "1.1.1.1", "port": 53},
    {"name": "GitHub Web Server", "host": "github.com", "port": 443},
]


def check_service(host, port, timeout=2):
  try:
    with socket.create_connection((host, port), timeout=timeout):
      return "Online"
  except Exception:
    logging.warning(f"Service Down: {host}:{port} is unreachable.")
    return "Offline"


@app.route("/api/status")
def get_status():
  cpu_usage = psutil.cpu_percent(interval=0.5)
  ram_usage = psutil.virtual_memory().percent
  disk_usage = psutil.disk_usage("/").percent

  network_status = []
  for target in TARGETS:
    status = check_service(target["host"], target["port"])
    network_status.append({
        "name": target["name"],
        "host": f"{target['host']}:{target['port']}",
        "status": status,
    })

  return jsonify({
      "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
      "cpu": cpu_usage,
      "ram": ram_usage,
      "disk": disk_usage,
      "network": network_status,
  })


@app.route("/")
def index():
  return render_template("index.html")


if __name__ == "__main__":
  app.run(port=5000)
  