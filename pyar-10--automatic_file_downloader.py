"""
Programmer: python_scripts (Abhijith Warrier)

PYTHON SCRIPT TO DOWNLOAD FILES FROM URLS WITH ORGANIZED NAMING 🐍⬇️📁

This script downloads files from a list of URLs and saves them
with structured filenames in a target folder. Useful for reports,
assets, datasets, and automation workflows.
"""

from pathlib import Path
from datetime import datetime
import requests

# --- Step 1: Configuration ---

# Folder where downloaded files should be saved
DOWNLOAD_FOLDER = Path("<YOUR_DESIRED_DOWNLOADS_FOLDER>")

# List of file URLs to download
URLS = [
    "https://example.com/file1.pdf",
    "https://example.com/file2.jpg",
    "https://example.com/file3.csv",
]

# Ensure download folder exists
DOWNLOAD_FOLDER.mkdir(exist_ok=True)

# --- Step 2: Download files ---
for index, url in enumerate(URLS, start=1):
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()

        # Try to get file extension from URL
        extension = Path(url).suffix or ".bin"

        # Create organized filename with timestamp + index
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"download_{index}_{timestamp}{extension}"

        output_path = DOWNLOAD_FOLDER / filename

        # Save file content
        with output_path.open("wb") as f:
            f.write(response.content)

        print(f"File Downloaded: {filename}")

    except Exception as e:
        print(f"Failed to download from {url}")
        print(f"Error: {e}")

print("\nFile download process completed.")
