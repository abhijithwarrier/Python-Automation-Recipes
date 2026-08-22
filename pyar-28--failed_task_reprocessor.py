"""
Programmer: python_scripts (Abhijith Warrier)

PYTHON SCRIPT TO RETRY FAILED AUTOMATION TASKS 🐍🔁📄

This script reads an audit log, identifies failed tasks,
re-executes them, and records the retry results.
Useful for workflow recovery, scheduled jobs,
and production automation systems.
"""

# Import the necessary packages
import csv
import time
import random
from pathlib import Path

# --- Step 1: Configure audit files ---
AUDIT_LOG = Path("task_audit_log.csv")
RETRY_LOG = Path("retry_audit_log.csv")

# --- Step 2: Define sample task implementations ---
def backup_task():
    print("Running backup task...")
    time.sleep(1)

def report_task():
    print("Generating report...")
    time.sleep(2)

def unstable_task():
    print("Retrying unstable task...")
    time.sleep(1)

    # Simulate random success/failure
    if random.random() < 0.4:
        raise Exception("Temporary failure")

# --- Step 3: Register available tasks ---
TASK_REGISTRY = {
    "backup_task": backup_task,
    "report_task": report_task,
    "unstable_task": unstable_task,
}

# --- Step 4: Create retry log if needed ---
if not RETRY_LOG.exists():
    with RETRY_LOG.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([
            "Task",
            "Retry Status"
        ])

# --- Step 5: Read failed tasks from audit log ---
with AUDIT_LOG.open("r", newline="", encoding="utf-8") as file:

    reader = csv.DictReader(file)

    for row in reader:
        if row["status"] != "FAILED":
            continue

        task_name = row["task_name"]
        print(f"\nRetrying: {task_name}")

        try:
            TASK_REGISTRY[task_name]()
            retry_status = "SUCCESS"
            print("Retry successful")

        except Exception:
            retry_status = "FAILED"
            print("Retry failed")

        # Record retry result
        with RETRY_LOG.open("a", newline="", encoding="utf-8") as retry_file:
            writer = csv.writer(retry_file)
            writer.writerow([
                task_name,
                retry_status
            ])

print("\nFailed task reprocessing completed.")
