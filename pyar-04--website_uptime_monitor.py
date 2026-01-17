"""
Programmer: python_scripts (Abhijith Warrier)

PYTHON SCRIPT TO MONITOR WEBSITE UPTIME AND LOG DOWNTIME 🐍🌐📉

This script periodically checks a website and logs downtime events
to a file. Ideal for basic monitoring of services, APIs, or websites.
"""

import requests
import time
from datetime import datetime
from pathlib import Path

# --- Step 1: Configuration ---

# Website to monitor
URL = "https://awdevrethought.com"  # change this to your desired website

# Time between checks (in seconds)
CHECK_INTERVAL = 60  # 1 minute

# Log file for downtime events
LOG_FILE = Path("uptime_log.txt")

# Request timeout (seconds)
TIMEOUT = 10

print(f"Monitoring uptime for: {URL}")
print(f"Check interval: {CHECK_INTERVAL} seconds\n")

# --- Step 2: Monitoring loop ---
while True:
    try:
        response = requests.get(URL, timeout=TIMEOUT)

        if response.status_code == 200:
            print(f"[{datetime.now()}] ✅ WEBSITE IS UP!")
        else:
            raise Exception(f"Status code: {response.status_code}")

    except Exception as e:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = f"[{timestamp}] ❌ WEBSITE IS DOWN! – {e}"

        # Log downtime event
        with LOG_FILE.open("a") as f:
            f.write(message + "\n")

        print(message)

    time.sleep(CHECK_INTERVAL)
