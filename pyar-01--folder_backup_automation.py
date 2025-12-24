"""
Programmer: python_scripts (Abhijith Warrier)

PYTHON SCRIPT TO BACK UP A FOLDER AS A TIMESTAMPED ZIP 🐍🗂️📦

This script creates a ZIP backup of a target folder and saves it
with a timestamped filename. Perfect for automating daily or
project-based backups.
"""

import shutil
from pathlib import Path
from datetime import datetime

# --- Step 1: Configure paths ---

# Folder you want to back up
SOURCE_FOLDER = Path("/Users/abhijith/Documents/my_project")  # 🔁 change this

# Where backups should be stored
BACKUP_FOLDER = Path("/Users/abhijith/Documents/backups")     # 🔁 change this

# Ensure backup directory exists
BACKUP_FOLDER.mkdir(parents=True, exist_ok=True)

# --- Step 2: Generate timestamp ---
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Backup file name (without extension)
backup_name = f"{SOURCE_FOLDER.name}_backup_{timestamp}"

# Full output path (without .zip)
backup_path = BACKUP_FOLDER / backup_name

# --- Step 3: Create ZIP archive ---
shutil.make_archive(
    base_name=str(backup_path),
    format="zip",
    root_dir=SOURCE_FOLDER
)

print(f"✅ Backup created successfully:")
print(f"📦 {backup_path}.zip")
