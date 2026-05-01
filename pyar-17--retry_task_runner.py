"""
Programmer: python_scripts (Abhijith Warrier)

PYTHON SCRIPT TO ADD RETRY LOGIC AND RESILIENCE TO TASKS 🐍🔁⚙️

This script demonstrates how to run tasks with retry logic,
delays between attempts, and proper failure handling.
Useful for APIs, file operations, and automation workflows.
"""

import time
import random
from datetime import datetime

# --- Step 1: Define a sample unstable task ---
def unstable_task():
    print("Running unstable task...")

    # Simulate random failure
    if random.random() < 0.7:
        raise Exception("Simulated failure")

    print("Task succeeded!")

# --- Step 2: Retry wrapper ---
def run_with_retry(task_func, max_retries=3, delay=2):
    attempt = 0

    while attempt < max_retries:
        try:
            print(f"\n▶Attempt {attempt + 1}")
            task_func()
            return True

        except Exception as e:
            print(f"Error: {e}")
            attempt += 1

            if attempt < max_retries:
                print(f"Retrying in {delay} seconds...")
                time.sleep(delay)
            else:
                print("Max retries reached. Task failed.")

    return False

# --- Step 3: Execute task with retry ---
print(f"Starting task at {datetime.now()}\n")
run_with_retry(unstable_task, max_retries=5, delay=3)
print("\nExecution completed.")
