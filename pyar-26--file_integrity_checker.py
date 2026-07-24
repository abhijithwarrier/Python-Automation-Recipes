"""
Programmer: python_scripts (Abhijith Warrier)

PYTHON SCRIPT TO GENERATE FILE INTEGRITY REPORTS 🐍🔒📂

This script scans a directory, calculates SHA-256 hashes for each
file, and exports the results to a CSV report for future integrity
verification.
"""

# Import hashlib for generating SHA-256 hashes
import hashlib

# Import csv for writing reports
import csv

# Import Path for file handling
from pathlib import Path

# --- Step 1: Configure directories ---
TARGET_DIRECTORY = Path("sample_files")
REPORT_FILE = Path("file_integrity_report.csv")

# Create sample directory if it doesn't exist
TARGET_DIRECTORY.mkdir(exist_ok=True)

# --- Step 2: Generate SHA-256 hash ---
def calculate_hash(file_path):

    sha256 = hashlib.sha256()

    with file_path.open("rb") as file:

        while chunk := file.read(4096):
            sha256.update(chunk)

    return sha256.hexdigest()

# --- Step 3: Scan files and generate report ---
with REPORT_FILE.open("w", newline="", encoding="utf-8") as csv_file:

    writer = csv.writer(csv_file)

    writer.writerow([
        "Filename",
        "Size (Bytes)",
        "SHA-256"
    ])

    for file_path in TARGET_DIRECTORY.rglob("*"):

        if file_path.is_file():

            checksum = calculate_hash(file_path)

            writer.writerow([
                file_path.name,
                file_path.stat().st_size,
                checksum
            ])

            print(f"{file_path.name}")
            print(f"{checksum}\n")

# --- Step 4: Finish ---
print("File integrity report generated successfully.")
print(REPORT_FILE.resolve())
