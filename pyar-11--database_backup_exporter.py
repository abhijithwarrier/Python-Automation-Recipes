"""
Programmer: python_scripts (Abhijith Warrier)

PYTHON SCRIPT TO EXPORT A DATABASE BACKUP AUTOMATICALLY 🐍🗄️📦

This script runs a PostgreSQL database dump command and saves the
backup with a timestamped filename. Useful for scheduled backups,
local safety copies, and recovery workflows.
"""

from pathlib import Path
from datetime import datetime
import subprocess
import os

# --- Step 1: Configuration ---

# Database connection details
DB_NAME = "db_name"         # 🔁 Set this to your database name
DB_USER = "db_username"     # 🔁 Set this to your database username
DB_HOST = "localhost"
DB_PORT = "5432"

# Password should be set in environment variable for security
DB_PASSWORD = "db_password"   # 🔁 better: use os.environ.get("PGPASSWORD")

# Backup output folder
BACKUP_FOLDER = Path("db_backups")
BACKUP_FOLDER.mkdir(exist_ok=True)

# --- Step 2: Create timestamped backup file name ---
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
backup_file = BACKUP_FOLDER / f"{DB_NAME}_backup_{timestamp}.sql"

# --- Step 3: Build pg_dump command ---
command = [
    "pg_dump",
    "-h", DB_HOST,
    "-p", DB_PORT,
    "-U", DB_USER,
    "-d", DB_NAME,
    "-f", str(backup_file)
]

# --- Step 4: Run backup command ---
try:
    env = os.environ.copy()
    env["PGPASSWORD"] = DB_PASSWORD

    subprocess.run(command, check=True, env=env)

    print(f"Database backup created successfully:")
    print(f"{backup_file}")

except subprocess.CalledProcessError as e:
    print("Database backup failed.")
    print(f"Error: {e}")
