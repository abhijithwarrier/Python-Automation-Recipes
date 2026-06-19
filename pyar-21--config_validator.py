"""
Programmer: python_scripts (Abhijith Warrier)

PYTHON SCRIPT TO VALIDATE JSON CONFIGS BEFORE EXECUTION 🐍⚙️✅

This script validates a JSON configuration file before running
an automation workflow. It checks required fields, data types,
and basic config rules to prevent runtime failures.
"""

import json
from pathlib import Path

# --- Step 1: Configure config file path ---
CONFIG_FILE = Path("config.json")

# --- Step 2: Define required config schema ---
REQUIRED_FIELDS = {
    "workflow_name": str,
    "enabled": bool,
    "tasks": list,
}

# --- Step 3: Load JSON config ---
def load_config(file_path):
    """
    Load and return JSON config data.
    """
    if not file_path.exists():
        raise FileNotFoundError(f"Config file not found: {file_path}")

    with file_path.open("r", encoding="utf-8") as file:
        return json.load(file)

# --- Step 4: Validate config structure ---
def validate_config(config):
    """
    Validate required fields and expected data types.
    """
    errors = []

    for field, expected_type in REQUIRED_FIELDS.items():

        # Check if field exists
        if field not in config:
            errors.append(f"Missing required field: {field}")
            continue

        # Check if field has correct type
        if not isinstance(config[field], expected_type):
            errors.append(
                f"Invalid type for '{field}'. "
                f"Expected {expected_type.__name__}, got {type(config[field]).__name__}"
            )

    # Check that tasks list is not empty
    if "tasks" in config and isinstance(config["tasks"], list):
        if not config["tasks"]:
            errors.append("Tasks list cannot be empty.")

        # Check every task is a string
        for task in config["tasks"]:
            if not isinstance(task, str):
                errors.append("Every task inside 'tasks' must be a string.")

    return errors

# --- Step 5: Run validation ---
try:
    config_data = load_config(CONFIG_FILE)
    validation_errors = validate_config(config_data)

    if validation_errors:
        print("Config validation failed:\n")

        for error in validation_errors:
            print(f"- {error}")

    else:
        print("Config validation passed.")
        print(f"Workflow ready: {config_data['workflow_name']}")

except json.JSONDecodeError as e:
    print("Invalid JSON format.")
    print(f"Error: {e}")

except Exception as e:
    print("Validation failed.")
    print(f"Error: {e}")
