"""
Programmer: python_scripts (Abhijith Warrier)

PYTHON SCRIPT TO TRACK TASK EXECUTION HISTORY AND OUTCOMES 🐍🧾📊

This script runs automation tasks and records their execution history
into a CSV audit log. It tracks start time, end time, duration,
status, and error messages for each task.
"""

import csv
import time
import random
from pathlib import Path
from datetime import datetime

# --- Step 1: Audit log configuration ---
AUDIT_LOG_FILE = Path("task_audit_log.csv")

# CSV columns for tracking task execution
FIELDNAMES = [
    "task_name",
    "start_time",
    "end_time",
    "duration_seconds",
    "status",
    "error_message",
]

# --- Step 2: Sample automation tasks ---
def backup_task():
    print("Running backup task...")
    time.sleep(1)

def report_task():
    print("Running report generation task...")
    time.sleep(2)

def unstable_task():
    print("Running unstable task...")
    time.sleep(1)

    # Simulate random failure
    if random.random() < 0.5:
        raise Exception("Simulated task failure")

# --- Step 3: Initialize audit log file ---
def initialize_audit_log():
    """
    Create the audit log file with headers if it does not already exist.
    """
    if not AUDIT_LOG_FILE.exists():
        with AUDIT_LOG_FILE.open("w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()

# --- Step 4: Write task result to audit log ---
def write_audit_log(record):
    """
    Append a task execution record to the CSV audit log.
    """
    with AUDIT_LOG_FILE.open("a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writerow(record)

# --- Step 5: Run task with audit tracking ---
def run_with_audit(task_name, task_function):
    """
    Run a task and record execution details including status,
    duration, timestamps, and error message if it fails.
    """
    start = datetime.now()
    status = "SUCCESS"
    error_message = ""

    try:
        task_function()

    except Exception as e:
        status = "FAILED"
        error_message = str(e)

    end = datetime.now()
    duration = (end - start).total_seconds()

    record = {
        "task_name": task_name,
        "start_time": start.strftime("%Y-%m-%d %H:%M:%S"),
        "end_time": end.strftime("%Y-%m-%d %H:%M:%S"),
        "duration_seconds": round(duration, 2),
        "status": status,
        "error_message": error_message,
    }

    write_audit_log(record)

    print(f"Logged: {task_name} -> {status}")

# --- Step 6: Run multiple tasks ---
initialize_audit_log()

tasks = {
    "backup_task": backup_task,
    "report_task": report_task,
    "unstable_task": unstable_task,
}

for task_name, task_function in tasks.items():
    run_with_audit(task_name, task_function)

print(f"\nAudit log updated: {AUDIT_LOG_FILE}")
