"""
Programmer: python_scripts (Abhijith Warrier)

PYTHON SCRIPT TO MONITOR SYSTEM HEALTH AND SEND ALERTS 🐍🖥️🚨

This script monitors CPU and RAM usage and logs an alert
if usage exceeds defined thresholds. Can be extended
to send email or Slack notifications.
"""

import psutil
import time
from datetime import datetime
from pathlib import Path

# --- Step 1: Configuration ---

CPU_THRESHOLD = 80        # Alert if CPU usage > 80%
RAM_THRESHOLD = 80        # Alert if RAM usage > 80%
CHECK_INTERVAL = 10       # Seconds between checks

LOG_FILE = Path("system_health_log.txt")

print("System Health Monitor Started...\n")

# --- Step 2: Monitoring loop ---
while True:

    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if cpu_usage > CPU_THRESHOLD or memory_usage > RAM_THRESHOLD:

        alert_message = (
            f"[{timestamp}] ALERT! "
            f"CPU: {cpu_usage}% | RAM: {memory_usage}%"
        )

        print(alert_message)

        # Log alert
        with LOG_FILE.open("a") as f:
            f.write(alert_message + "\n")

        # Note: Extend here to send email or Slack alert

    else:
        print(f"[{timestamp}] CPU: {cpu_usage}% | RAM: {memory_usage}%")

    time.sleep(CHECK_INTERVAL)
