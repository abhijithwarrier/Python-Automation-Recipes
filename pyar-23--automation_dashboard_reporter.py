"""
Programmer: python_scripts (Abhijith Warrier)

PYTHON SCRIPT TO GENERATE AN HTML AUTOMATION DASHBOARD 🐍📊🌐

This script generates an HTML dashboard showing automation task
execution history. Useful for monitoring scheduled jobs,
automation workflows, and execution summaries.
"""

from pathlib import Path
from datetime import datetime

# --- Step 1: Sample execution results ---
task_results = [
    {
        "task": "Backup Folder",
        "status": "SUCCESS",
        "duration": "2.3 sec",
    },
    {
        "task": "Generate Report",
        "status": "SUCCESS",
        "duration": "1.7 sec",
    },
    {
        "task": "Send Email",
        "status": "FAILED",
        "duration": "0.5 sec",
    },
    {
        "task": "Cleanup Logs",
        "status": "SUCCESS",
        "duration": "0.9 sec",
    },
]

# Output HTML file
REPORT_FILE = Path("automation_dashboard.html")

# Current timestamp
generated_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# --- Step 2: Build HTML table rows ---
rows = ""

for task in task_results:

    color = "#28a745" if task["status"] == "SUCCESS" else "#dc3545"

    rows += f"""
    <tr>
        <td>{task['task']}</td>
        <td style="color:{color}; font-weight:bold;">
            {task['status']}
        </td>
        <td>{task['duration']}</td>
    </tr>
    """

# --- Step 3: Build HTML document ---
html = f"""
<!DOCTYPE html>
<html>

<head>
    <title>Automation Dashboard</title>

    <style>

        body {{
            font-family: Arial, sans-serif;
            margin: 40px;
            background: #f7f7f7;
        }}

        h1 {{
            color: #333;
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            background: white;
        }}

        th, td {{
            border: 1px solid #ddd;
            padding: 12px;
            text-align: left;
        }}

        th {{
            background: #222;
            color: white;
        }}

    </style>

</head>

<body>

<h1>📊 Automation Dashboard</h1>

<p><strong>Generated:</strong> {generated_time}</p>

<table>

<tr>
    <th>Task</th>
    <th>Status</th>
    <th>Duration</th>
</tr>

{rows}

</table>

</body>

</html>
"""

# --- Step 4: Save HTML report ---
REPORT_FILE.write_text(html, encoding="utf-8")

print(f"Dashboard generated successfully:")
print(REPORT_FILE.resolve())
