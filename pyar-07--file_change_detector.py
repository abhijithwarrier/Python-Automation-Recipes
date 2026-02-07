"""
Programmer: python_scripts (Abhijith Warrier)

PYTHON SCRIPT TO DETECT FILE CHANGES AND TRIGGER ACTIONS 🐍👀📂

This script monitors a folder for file modifications and
triggers actions when changes are detected. Ideal for
config monitoring, automation triggers, and workflows.
"""

import time
from pathlib import Path
from datetime import datetime

# --- Step 1: Configuration ---

# Folder to monitor
WATCH_FOLDER = Path("<YOUR_PREFERRED_FOLDER_LOCATION>")  # Change this

# Polling interval (seconds)
CHECK_INTERVAL = 5

# Store last known modification times
file_mod_times = {}

print(f"👀 Watching folder: {WATCH_FOLDER}\n")

# --- Step 2: Monitoring loop ---
while True:
    for file_path in WATCH_FOLDER.glob("*"):
        if file_path.is_file():

            last_modified = file_path.stat().st_mtime

            # First time seeing the file
            if file_path not in file_mod_times:
                file_mod_times[file_path] = last_modified
                continue

            # Detect modification
            if last_modified != file_mod_times[file_path]:
                file_mod_times[file_path] = last_modified
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                print(f"[{timestamp}] File changed: {file_path.name}")

                # Trigger custom action here
                # e.g., backup file, reload config, send alert

    time.sleep(CHECK_INTERVAL)
