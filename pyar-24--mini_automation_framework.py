"""
Programmer: python_scripts (Abhijith Warrier)

PYTHON SCRIPT TO BUILD A MINI AUTOMATION FRAMEWORK 🐍🏗️⚙️

This script demonstrates a lightweight automation framework that
combines task registration, workflow execution, retries, and
audit logging into a reusable architecture.
"""

import csv
import time
from pathlib import Path
from datetime import datetime

# --- Step 1: Audit log configuration ---
AUDIT_LOG = Path("automation_audit.csv")

if not AUDIT_LOG.exists():
    with AUDIT_LOG.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(
            ["Task", "Status", "Start Time", "End Time", "Duration (s)"]
        )

# --- Step 2: Define automation tasks ---
def backup_folder():
    print("Backing up folder...")
    time.sleep(1)

def clean_logs():
    print("Cleaning logs...")
    time.sleep(1)

def generate_report():
    print("Generating report...")
    time.sleep(2)

# --- Step 3: Task registry ---
TASKS = {
    "backup_folder": backup_folder,
    "clean_logs": clean_logs,
    "generate_report": generate_report,
}

# --- Step 4: Retry wrapper ---
def execute_task(task_name, retries=3):

    task = TASKS[task_name]

    for attempt in range(1, retries + 1):
        start = datetime.now()

        try:
            print(f"\n▶{task_name} (Attempt {attempt})")
            task()
            end = datetime.now()
            duration = (end - start).total_seconds()
            log_execution(
                task_name,
                "SUCCESS",
                start,
                end,
                duration,
            )
            print("Success")
            return

        except Exception:
            print("Failed")

            if attempt == retries:
                end = datetime.now()
                duration = (end - start).total_seconds()
                log_execution(
                    task_name,
                    "FAILED",
                    start,
                    end,
                    duration,
                )

# --- Step 5: Audit logger ---
def log_execution(task, status, start, end, duration):

    with AUDIT_LOG.open("a", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow([
            task,
            status,
            start.strftime("%Y-%m-%d %H:%M:%S"),
            end.strftime("%Y-%m-%d %H:%M:%S"),
            round(duration, 2)
        ])

# --- Step 6: Workflow execution ---
workflow = [
    "backup_folder",
    "clean_logs",
    "generate_report",
]

print("Starting Automation Framework\n")

for task_name in workflow:
    execute_task(task_name)

print("\nWorkflow completed successfully.")
print(f"Audit log saved to: {AUDIT_LOG}")
