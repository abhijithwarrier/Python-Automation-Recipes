"""
Programmer: python_scripts (Abhijith Warrier)

PYTHON SCRIPT TO VALIDATE REQUIRED ENVIRONMENT VARIABLES 🐍🔐⚙️

This script checks whether all required environment variables
are available before executing an automation workflow.
"""

# Import os for accessing environment variables
import os

# --- Step 1: Define required environment variables ---
REQUIRED_VARIABLES = [
    "API_KEY",
    "DATABASE_URL",
    "SMTP_USERNAME",
    "SMTP_PASSWORD",
    "BACKUP_DIRECTORY",
]

# --- Step 2: Validate environment variables ---
missing_variables = []

for variable in REQUIRED_VARIABLES:

    value = os.getenv(variable)

    if value is None or value.strip() == "":
        missing_variables.append(variable)

# --- Step 3: Display validation results ---
if missing_variables:

    print("Environment validation failed.\n")
    print("The following variables are missing:\n")

    for variable in missing_variables:
        print(f"• {variable}")

    raise SystemExit("\nPlease configure the missing variables and try again.")

print("All required environment variables are configured.")

# --- Step 4: Continue with automation workflow ---
print("\nStarting automation workflow...")

# Example automation entry point
print("Running scheduled tasks...")
