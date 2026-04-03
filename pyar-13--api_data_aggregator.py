"""
Programmer: python_scripts (Abhijith Warrier)

PYTHON SCRIPT TO FETCH DATA FROM MULTIPLE APIS AND COMBINE INTO A REPORT 🐍🌐📊

This script fetches data from multiple APIs (weather + crypto),
combines them into a single report, and prints the result.
Useful for dashboards, monitoring, and automation workflows.
"""

import requests
from datetime import datetime
from pathlib import Path

# --- Step 1: Configuration ---

CITY = "Bangalore"  # Change as needed
OUTPUT_FILE = Path("api_report.txt")

# --- Step 2: Fetch Weather Data ---
def get_weather(city):
    url = f"https://wttr.in/{city}?format=j1"
    response = requests.get(url, timeout=10)
    data = response.json()

    current = data["current_condition"][0]

    return {
        "temperature": current["temp_C"],
        "feels_like": current["FeelsLikeC"],
        "condition": current["weatherDesc"][0]["value"]
    }

# --- Step 3: Fetch Crypto Data ---
def get_bitcoin_price():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(url, timeout=10)
    data = response.json()

    return {
        "price_usd": data["bpi"]["USD"]["rate"]
    }

# --- Step 4: Combine Data ---
try:
    weather = get_weather(CITY)
    btc = get_bitcoin_price()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    report = f"""
📊 API Aggregated Report
------------------------
Time: {timestamp}

🌤️ Weather in {CITY}:
- Temperature: {weather['temperature']}°C
- Feels Like: {weather['feels_like']}°C
- Condition: {weather['condition']}

₿ Bitcoin Price:
- USD: ${btc['price_usd']}
"""

    print(report)

    # --- Step 5: Save Report ---
    with OUTPUT_FILE.open("w") as f:
        f.write(report)

    print(f"Report saved to: {OUTPUT_FILE}")

except Exception as e:
    print("Failed to fetch API data:", e)
