"""
Programmer: python_scripts (Abhijith Warrier)

PYTHON SCRIPT TO FIND AND HANDLE DUPLICATE FILES 🐍🧩📂

This script scans a folder, detects duplicate files based on content hash,
and either logs them or moves them into a separate folder.
Useful for cleanup, storage optimization, and backup hygiene.
"""

from pathlib import Path
import hashlib
import shutil

# --- Step 1: Configuration ---

# Folder to scan for duplicates
TARGET_FOLDER = Path("<YOUR_DESIRED FOLDER>")  # 🔁 Change this to your desired path

# Where duplicate files should be moved (used only if MOVE_DUPLICATES = True)
DUPLICATES_FOLDER = TARGET_FOLDER / "duplicates"

# Log file for duplicate entries
LOG_FILE = TARGET_FOLDER / "duplicate_files_log.txt"

# Action mode: True = move duplicates, False = just log them
MOVE_DUPLICATES = False

# Create duplicates folder if moving is enabled
if MOVE_DUPLICATES:
    DUPLICATES_FOLDER.mkdir(exist_ok=True)

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

# --- Step 3: Scan files and track hashes ---
seen_hashes = {}

with LOG_FILE.open("w") as log:
    log.write("Duplicate File Report\n")
    log.write("=====================\n\n")

    for file_path in TARGET_FOLDER.rglob("*"):
        if file_path.is_file():

            # Skip the log file itself and files inside duplicates folder
            if file_path == LOG_FILE or file_path.parent == DUPLICATES_FOLDER:
                continue

            file_hash = get_file_hash(file_path)

            if file_hash in seen_hashes:
                original_file = seen_hashes[file_hash]

                log.write(f"Duplicate: {file_path}\n")
                log.write(f"Original : {original_file}\n\n")

                print(f"Duplicate found: {file_path.name}")

                if MOVE_DUPLICATES:
                    destination = DUPLICATES_FOLDER / file_path.name
                    shutil.move(str(file_path), str(destination))
                    print(f"Moved to: {destination}")

            else:
                seen_hashes[file_hash] = file_path

print(f"\nScan complete. Report saved to: {LOG_FILE}")
