"""
Programmer: python_scripts (Abhijith Warrier)

PYTHON SCRIPT TO RUN TASKS FROM A JSON CONFIG FILE 🐍⚙️🧩

This script reads a workflow configuration file and executes enabled
tasks in order. Useful for building flexible automation workflows,
batch jobs, and mini workflow runners.
"""

import json
from pathlib import Path
from datetime import datetime

# --- Step 1: Configure config file path ---
CONFIG_FILE = Path("workflow_config.json")

# --- Step 2: Define task functions ---
def backup_folder():
    print("Running folder backup task...")
    # Add real backup logic here

def clean_logs():
    print("Running log cleanup task...")
    # Add real log cleaning logic here

def send_report():
    print("Running report email task...")
    # Add real email report logic here

# --- Step 3: Map task names from config to Python functions ---
TASK_REGISTRY = {
    "backup_folder": backup_folder,
    "clean_logs": clean_logs,
    "send_report": send_report,
}

# --- Step 4: Load workflow configuration ---
if not CONFIG_FILE.exists():
    raise FileNotFoundError(f"Config file not found: {CONFIG_FILE}")

with CONFIG_FILE.open("r", encoding="utf-8") as file:
    config = json.load(file)

workflow_name = config.get("workflow_name", "unnamed_workflow")
tasks = config.get("tasks", [])

print(f"Starting workflow: {workflow_name}")
print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

# --- Step 5: Execute enabled tasks in order ---
for task in tasks:
    task_name = task.get("name")
    enabled = task.get("enabled", False)

    if not enabled:
        print(f"Skipped disabled task: {task_name}")
        continue

    task_function = TASK_REGISTRY.get(task_name)

    if task_function:
        print(f"Executing task: {task_name}")
        task_function()
        print(f"Completed task: {task_name}\n")
    else:
        print(f"Unknown task: {task_name}\n")

print("Workflow execution completed.")
