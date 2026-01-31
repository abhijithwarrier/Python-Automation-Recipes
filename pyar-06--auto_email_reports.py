"""
Programmer: python_scripts (Abhijith Warrier)

PYTHON SCRIPT TO GENERATE AND EMAIL REPORTS AUTOMATICALLY 🐍📧📊

This script generates a simple report and sends it via email.
Ideal for daily summaries, automated metrics, and system reports.
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

# --- Step 1: Email configuration ---

SENDER_EMAIL = "your_email@gmail.com"        # Change this
SENDER_PASSWORD = "YOUR_APP_PASSWORD"        # Use app password
RECEIVER_EMAIL = "receiver@example.com"

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# --- Step 2: Generate report content ---
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

report_content = f"""
Daily Automation Report
-----------------------
Generated at: {now}

• All systems operational
• No errors detected
• Report generated automatically by Python
"""

# --- Step 3: Create email ---
message = MIMEMultipart()
message["From"] = SENDER_EMAIL
message["To"] = RECEIVER_EMAIL
message["Subject"] = "Automated Daily Report"

message.attach(MIMEText(report_content, "plain"))

# --- Step 4: Send email ---
try:
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(SENDER_EMAIL, SENDER_PASSWORD)
    server.send_message(message)
    server.quit()

    print("Report emailed successfully!")

except Exception as e:
    print("Failed to send email:", e)
