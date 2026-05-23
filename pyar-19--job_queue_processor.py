"""
Programmer: python_scripts (Abhijith Warrier)

PYTHON SCRIPT TO PROCESS TASKS FROM A JSON JOB QUEUE 🐍📋⚙️

This script reads jobs from a JSON queue file and executes them
one by one. Useful for workflow engines, automation pipelines,
batch processors, and background workers.
"""

import json
import time
from pathlib import Path
from datetime import datetime

# --- Step 1: Queue file configuration ---
QUEUE_FILE = Path("job_queue.json")

# --- Step 2: Define task handlers ---
def send_email(payload):
    print(f"Sending email to: {payload.get('to')}")
    time.sleep(1)

def generate_report(payload):
    print("Generating report...")
    time.sleep(2)

def cleanup_logs(payload):
    print("🧹 Cleaning log files...")
    time.sleep(1)

# --- Step 3: Task registry ---
TASK_REGISTRY = {
    "send_email": send_email,
    "generate_report": generate_report,
    "cleanup_logs": cleanup_logs,
}

# --- Step 4: Load queue file ---
if not QUEUE_FILE.exists():
    raise FileNotFoundError(f"Queue file not found: {QUEUE_FILE}")

with QUEUE_FILE.open("r", encoding="utf-8") as f:
    queue_data = json.load(f)

jobs = queue_data.get("jobs", [])

print(f"Job Queue Processor Started")
print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

# --- Step 5: Process jobs sequentially ---
for job in jobs:
    job_id = job.get("id")
    task_name = job.get("task")
    payload = job.get("payload", {})

    print(f"Processing Job #{job_id}: {task_name}")

    task_function = TASK_REGISTRY.get(task_name)

    if not task_function:
        print(f"Unknown task: {task_name}\n")
        continue

    try:
        task_function(payload)
        print(f"Job #{job_id} completed\n")

    except Exception as e:
        print(f"Job #{job_id} failed: {e}\n")

print("Queue processing completed.")
