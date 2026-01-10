"""
Programmer: python_scripts (Abhijith Warrier)

PYTHON SCRIPT TO CONVERT CSV DATA INTO A FORMATTED EXCEL REPORT 🐍📊📁

This script reads a CSV file and generates a clean Excel report
with basic formatting. Ideal for analytics exports, reports,
and data sharing workflows.
"""

import pandas as pd
from pathlib import Path

# --- Step 1: Configure paths ---

# Input CSV file
CSV_FILE = Path("data.csv")        # 🔁 change this

# Output Excel file
EXCEL_FILE = Path("report.xlsx")

# --- Step 2: Load CSV data ---
if not CSV_FILE.exists():
    raise FileNotFoundError(f"CSV file not found: {CSV_FILE}")

df = pd.read_csv(CSV_FILE)

# --- Step 3: Write to Excel with formatting ---
with pd.ExcelWriter(EXCEL_FILE, engine="xlsxwriter") as writer:
    df.to_excel(writer, index=False, sheet_name="Report")

    workbook = writer.book
    worksheet = writer.sheets["Report"]

    # Format header row
    header_format = workbook.add_format({
        "bold": True,
        "border": 1
    })

    for col_num, col_name in enumerate(df.columns):
        worksheet.write(0, col_num, col_name, header_format)

        # Auto-adjust column width
        max_len = max(
            df[col_name].astype(str).map(len).max(),
            len(col_name)
        )
        worksheet.set_column(col_num, col_num, max_len + 2)

print(f"✅ Excel report generated successfully: {EXCEL_FILE}")
