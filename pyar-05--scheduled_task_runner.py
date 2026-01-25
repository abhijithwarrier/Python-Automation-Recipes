"""
Programmer: python_scripts (Abhijith Warrier)

PYTHON SCRIPT TO RUN TASKS ON A SCHEDULE USING schedule 🐍⏱️📅

This script demonstrates how to schedule and run Python functions
at fixed intervals using the schedule library. Useful for periodic
automation tasks and background jobs.
"""

import schedule
import time
from datetime import datetime

# --- Step 1: Define the task ---
def run_task():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Task executed at {now}")

# --- Step 2: Schedule the task ---
schedule.every(1).minutes.do(run_task)          # Syntax to run every minute
# schedule.every().hour.do(run_task)            # Syntax to run every hour
# schedule.every().day.at("10:00").do(run_task) # Syntax to run every day

print("Scheduler started. Press Ctrl+C to stop.\n")

# --- Step 3: Run the scheduler loop ---
while True:
    schedule.run_pending()
    time.sleep(1)
