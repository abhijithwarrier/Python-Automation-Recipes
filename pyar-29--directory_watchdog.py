"""
Programmer: python_scripts (Abhijith Warrier)

PYTHON SCRIPT TO MONITOR A DIRECTORY FOR FILE CHANGES 🐍👀📂

This script watches a directory in real time and detects file
creation, modification, deletion, and movement events.
Useful for event-driven automation workflows.
"""

# Import time for keeping the observer alive
import time

# Import Path for directory handling
from pathlib import Path

# Import watchdog components
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# --- Step 1: Configure directory to monitor ---
WATCH_DIRECTORY = Path("watch_folder")

WATCH_DIRECTORY.mkdir(exist_ok=True)


# --- Step 2: Define event handler ---
class DirectoryEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        if not event.is_directory:
            print(f"Created : {event.src_path}")

    def on_modified(self, event):
        if not event.is_directory:
            print(f"Modified: {event.src_path}")

    def on_deleted(self, event):
        if not event.is_directory:
            print(f"Deleted : {event.src_path}")

    def on_moved(self, event):
        if not event.is_directory:
            print(f"Moved   : {event.src_path} → {event.dest_path}")


# --- Step 3: Start directory monitoring ---
observer = Observer()
observer.schedule(
    DirectoryEventHandler(),
    str(WATCH_DIRECTORY),
    recursive=True,
)

observer.start()

print(f"Watching: {WATCH_DIRECTORY.resolve()}")
print("Press Ctrl+C to stop.\n")

# --- Step 4: Keep monitoring ---
try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    observer.stop()

observer.join()

print("Directory monitoring stopped.")

