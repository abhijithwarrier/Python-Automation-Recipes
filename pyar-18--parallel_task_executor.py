"""
Programmer: python_scripts (Abhijith Warrier)

PYTHON SCRIPT TO RUN MULTIPLE TASKS CONCURRENTLY USING THREADS 🐍🧵⚙️

This script demonstrates how to execute independent tasks in parallel
using ThreadPoolExecutor. Useful for downloads, API calls, health checks,
file processing, and automation workflows.
"""

from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
import time
import random

# --- Step 1: Define sample automation tasks ---
def run_task(task_name: str) -> str:
    """
    Simulate an automation task that takes some time to finish.
    Replace this logic with real tasks like API calls, file checks,
    downloads, or report generation.
    """
    duration = random.randint(1, 5)

    print(f"Started: {task_name} | Estimated time: {duration}s")
    time.sleep(duration)

    return f"Completed: {task_name} in {duration}s"


# --- Step 2: Define the list of tasks to run ---
tasks = [
    "Download report",
    "Check website status",
    "Clean temporary files",
    "Generate summary",
    "Send notification",
]

# --- Step 3: Run tasks in parallel ---
print(f"Parallel execution started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

with ThreadPoolExecutor(max_workers=3) as executor:
    # Submit tasks to the thread pool
    future_to_task = {
        executor.submit(run_task, task): task
        for task in tasks
    }

    # Process results as each task completes
    for future in as_completed(future_to_task):
        task_name = future_to_task[future]

        try:
            result = future.result()
            print(result)

        except Exception as e:
            print(f"Failed: {task_name} | Error: {e}")

print("\nAll parallel tasks completed.")
