"""
Programmer: python_scripts (Abhijith Warrier)

PYTHON SCRIPT TO EXECUTE TASKS BASED ON DEPENDENCY ORDER 🐍🔗⚙️

This script loads a workflow configuration and executes tasks
only after all their dependencies have completed.
Useful for workflow orchestration, ETL pipelines,
and automation systems.
"""

import json
import time
from pathlib import Path

# --- Step 1: Configuration ---
WORKFLOW_FILE = Path("workflow.json")

# --- Step 2: Sample task implementations ---
def backup_database():
    print("Backing up database...")
    time.sleep(1)

def clean_logs():
    print("Cleaning logs...")
    time.sleep(1)

def generate_report():
    print("Generating report...")
    time.sleep(2)

def send_email():
    print("Sending report...")
    time.sleep(1)

# --- Step 3: Task registry ---
TASKS = {
    "backup_database": backup_database,
    "clean_logs": clean_logs,
    "generate_report": generate_report,
    "send_email": send_email,
}

# --- Step 4: Load workflow configuration ---
with WORKFLOW_FILE.open("r", encoding="utf-8") as file:
    workflow = json.load(file)

pending_tasks = workflow["tasks"]
completed_tasks = set()

print("Starting workflow...\n")

# --- Step 5: Execute tasks based on dependencies ---
while pending_tasks:

    progress = False

    for task in pending_tasks[:]:

        task_name = task["name"]
        dependencies = task.get("depends_on", [])

        # Check whether all dependencies have completed
        if all(dep in completed_tasks for dep in dependencies):

            print(f"Executing: {task_name}")

            TASKS[task_name]()

            print(f"Completed: {task_name}\n")

            completed_tasks.add(task_name)
            pending_tasks.remove(task)

            progress = True

    # Detect circular or invalid dependencies
    if not progress:
        raise RuntimeError(
            "Unable to continue. Check for circular or missing dependencies."
        )

print("Workflow completed successfully.")
