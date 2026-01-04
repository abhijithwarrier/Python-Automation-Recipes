"""
Programmer: python_scripts (Abhijith Warrier)

PYTHON SCRIPT TO DELETE OR ARCHIVE OLD LOG FILES 🐍🧹📄

This script scans a log directory and removes or archives log files
older than a specified number of days. Ideal for servers, local dev
machines, and long-running projects.
"""

from pathlib import Path
from datetime import datetime, timedelta
import shutil

# --- Step 1: Configuration ---

# Folder containing log files
LOG_FOLDER = Path("<YOUR_CHOICE_OF_PATH>")  # 🔁 change this

# Archive folder (used if ARCHIVE_OLD_LOGS = True)
ARCHIVE_FOLDER = LOG_FOLDER / "archive"

# Number of days to keep logs
RETENTION_DAYS = 7

# Action mode: True = archive, False = delete
ARCHIVE_OLD_LOGS = True

# Ensure archive directory exists if needed
if ARCHIVE_OLD_LOGS:
    ARCHIVE_FOLDER.mkdir(exist_ok=True)

# --- Step 2: Calculate cutoff date ---
cutoff_date = datetime.now() - timedelta(days=RETENTION_DAYS)

# --- Step 3: Process log files ---
for log_file in LOG_FOLDER.glob("*.log"):

    # Get last modified time
    last_modified = datetime.fromtimestamp(log_file.stat().st_mtime)

    # Check if file is older than retention period
    if last_modified < cutoff_date:

        if ARCHIVE_OLD_LOGS:
            destination = ARCHIVE_FOLDER / log_file.name
            shutil.move(str(log_file), str(destination))
            print(f"📦 Archived: {log_file.name}")
        else:
            log_file.unlink()
            print(f"🗑️ Deleted: {log_file.name}")

print("\n✅ Log file cleanup completed.")
