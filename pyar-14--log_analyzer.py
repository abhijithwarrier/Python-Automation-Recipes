"""
Programmer: python_scripts (Abhijith Warrier)

PYTHON SCRIPT TO PARSE LOG FILES AND GENERATE ERROR OR USAGE SUMMARIES 🐍📄📊

This script reads a log file, counts log levels like INFO, WARNING,
ERROR, and CRITICAL, and writes a simple summary report.
Useful for debugging, monitoring, and operational analysis.
"""

from pathlib import Path
from collections import Counter

# --- Step 1: Configuration ---

# Path to the log file you want to analyze
LOG_FILE = Path("app.log")  # Change this

# Output file for the generated summary
REPORT_FILE = Path("log_summary_report.txt")

# --- Step 2: Validate input file ---
if not LOG_FILE.exists():
    raise FileNotFoundError(f"Log file not found: {LOG_FILE}")

# --- Step 3: Initialize counters and storage ---
log_levels = Counter()
total_lines = 0
error_lines = []

# --- Step 4: Read and analyze the log file ---
with LOG_FILE.open("r", encoding="utf-8") as f:
    for line in f:
        total_lines += 1
        line = line.strip()

        # Count common log levels
        if "INFO" in line:
            log_levels["INFO"] += 1
        if "WARNING" in line:
            log_levels["WARNING"] += 1
        if "ERROR" in line:
            log_levels["ERROR"] += 1
            error_lines.append(line)
        if "CRITICAL" in line:
            log_levels["CRITICAL"] += 1
            error_lines.append(line)

# --- Step 5: Build summary report ---
report = []
report.append("Log Analysis Report")
report.append("----------------------")
report.append(f"Total lines processed: {total_lines}")
report.append(f"INFO entries        : {log_levels['INFO']}")
report.append(f"WARNING entries     : {log_levels['WARNING']}")
report.append(f"ERROR entries       : {log_levels['ERROR']}")
report.append(f"CRITICAL entries    : {log_levels['CRITICAL']}")
report.append("")
report.append("Error / Critical Entries:")
report.append("---------------------------")

if error_lines:
    report.extend(error_lines[:10])  # show first 10 error lines
else:
    report.append("No ERROR or CRITICAL entries found.")

report_text = "\n".join(report)

# --- Step 6: Print and save report ---
print(report_text)

with REPORT_FILE.open("w", encoding="utf-8") as f:
    f.write(report_text)

print(f"\nSummary report saved to: {REPORT_FILE}")
