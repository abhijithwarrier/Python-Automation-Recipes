"""
Programmer: python_scripts (Abhijith Warrier)

PYTHON SCRIPT TO PREVENT MULTIPLE AUTOMATION INSTANCES 🐍🔒⚙️

This script uses a lock file to ensure that only one instance
of an automation workflow runs at a time.
Useful for scheduled jobs, ETL pipelines, backups,
and production automation systems.
"""

# Import Path for file handling
from pathlib import Path

# Import time to simulate work
import time

# --- Step 1: Configure lock file ---
LOCK_FILE = Path("automation.lock")

# --- Step 2: Check if another instance is already running ---
if LOCK_FILE.exists():
    print("Another automation instance is already running.")
    print("Exiting safely...")
    raise SystemExit()

# --- Step 3: Create lock file ---
LOCK_FILE.write_text("Automation is running")

print("Lock acquired.")
print("Starting automation...\n")

try:

    # -----------------------------
    # Simulated automation workflow
    # -----------------------------
    for step in range(1, 6):

        print(f"Running task {step}...")
        time.sleep(1)

    print("\nAutomation completed successfully.")

finally:

    # --- Step 4: Always remove lock file ---
    if LOCK_FILE.exists():
        LOCK_FILE.unlink()

    print("Lock released.")
