"""
Programmer: python_scripts (Abhijith Warrier)

PYTHON SCRIPT TO COMPARE TWO FOLDERS AND DETECT MISSING OR CHANGED FILES 🐍📂🔍

This script scans two folders recursively, compares matching files by
relative path, and reports files that are missing or different.
Useful for backup validation, folder sync checks, and audit workflows.
"""

from pathlib import Path
import hashlib

# --- Step 1: Configure folders ---

# First folder to compare
SOURCE_FOLDER = Path("<YOUR_DESIRED_SOURCE_FOLDER>")  # change this

# Second folder to compare
TARGET_FOLDER = Path("<YOUR_DESIRED_DESTINATION_FOLDER")  # change this

# --- Step 2: Helper function to hash file contents ---
def get_file_hash(file_path: Path) -> str:
    """
    Generate a SHA-256 hash for a file's contents.
    Files with the same content will produce the same hash.
    """
    hasher = hashlib.sha256()

    with file_path.open("rb") as f:
        while chunk := f.read(8192):
            hasher.update(chunk)

    return hasher.hexdigest()

# --- Step 3: Build relative file maps for both folders ---
source_files = {
    file.relative_to(SOURCE_FOLDER): file
    for file in SOURCE_FOLDER.rglob("*")
    if file.is_file()
}

target_files = {
    file.relative_to(TARGET_FOLDER): file
    for file in TARGET_FOLDER.rglob("*")
    if file.is_file()
}

# --- Step 4: Compare file sets ---
all_relative_paths = set(source_files.keys()) | set(target_files.keys())

missing_in_target = []
missing_in_source = []
changed_files = []

for rel_path in sorted(all_relative_paths):
    source_file = source_files.get(rel_path)
    target_file = target_files.get(rel_path)

    # File exists in source but not in target
    if source_file and not target_file:
        missing_in_target.append(rel_path)

    # File exists in target but not in source
    elif target_file and not source_file:
        missing_in_source.append(rel_path)

    # File exists in both; compare contents
    else:
        if get_file_hash(source_file) != get_file_hash(target_file):
            changed_files.append(rel_path)

# --- Step 5: Print results ---
print("Folder Sync Check Report\n")

if missing_in_target:
    print("Missing in TARGET_FOLDER:")
    for path in missing_in_target:
        print(f"   - {path}")
    print()

if missing_in_source:
    print("Missing in SOURCE_FOLDER:")
    for path in missing_in_source:
        print(f"   - {path}")
    print()

if changed_files:
    print("Changed files:")
    for path in changed_files:
        print(f"   - {path}")
    print()

if not missing_in_target and not missing_in_source and not changed_files:
    print("Both folders are fully in sync.")
