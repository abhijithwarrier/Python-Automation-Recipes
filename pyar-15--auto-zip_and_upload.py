"""
Programmer: python_scripts (Abhijith Warrier)

PYTHON SCRIPT TO ZIP A FOLDER AND UPLOAD IT TO CLOUD STORAGE 🐍📦☁️

This script creates a timestamped ZIP archive of a folder and uploads
it to an S3 bucket using boto3. Useful for backups, exports,
and automated archival workflows.
"""

from pathlib import Path
from datetime import datetime
import shutil
import boto3

# --- Step 1: Configuration ---

# Folder you want to compress
SOURCE_FOLDER = Path("<YOUR_DESIRED_FOLDER>/my_project")  # Change this

# Temporary folder to store generated ZIP files
OUTPUT_FOLDER = Path("archives")
OUTPUT_FOLDER.mkdir(exist_ok=True)

# AWS S3 configuration
BUCKET_NAME = "your-s3-bucket-name"   # Change this
S3_FOLDER = "backups"                 # Folder path inside S3 bucket

# --- Step 2: Generate timestamped ZIP filename ---
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
zip_name = f"{SOURCE_FOLDER.name}_{timestamp}"
zip_path_without_ext = OUTPUT_FOLDER / zip_name

# --- Step 3: Create ZIP archive ---
archive_path = shutil.make_archive(
    base_name=str(zip_path_without_ext),
    format="zip",
    root_dir=SOURCE_FOLDER
)

print(f"📦 ZIP archive created: {archive_path}")

# --- Step 4: Upload ZIP to S3 ---
try:
    s3_client = boto3.client("s3")

    s3_key = f"{S3_FOLDER}/{Path(archive_path).name}"
    s3_client.upload_file(archive_path, BUCKET_NAME, s3_key)

    print(f"   Uploaded to S3 successfully:")
    print(f"   Bucket: {BUCKET_NAME}")
    print(f"   Key   : {s3_key}")

except Exception as e:
    print(f"Upload failed.")
    print(f"Error: {e}")
