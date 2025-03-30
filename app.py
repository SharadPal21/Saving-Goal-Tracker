import os
import json
from flask import Flask
from utils.goal_manager import GoalManager
from utils.expense_tracker import ExpenseTracker
from utils.currency_converter import CurrencyConverter

# Define file paths
GOAL_FILE = "data/goals.json"
EXPENSE_FILE = "data/expenses.json"
EXCHANGE_RATE_FILE = "data/exchange_rates.json"

def ensure_file_exists(file_path, default_data):
    """Ensure the file and its directory exist. Initialize with default data if missing."""
    folder = os.path.dirname(file_path)
    if not os.path.exists(folder):
        os.makedirs(folder)

    if not os.path.exists(file_path):
        with open(file_path, "w") as file:
            json.dump(default_data, file)

# Ensure required files exist
ensure_file_exists(GOAL_FILE, [])
ensure_file_exists(EXPENSE_FILE, [])
ensure_file_exists(EXCHANGE_RATE_FILE, {})

# Initialize app
app = Flask(__name__)

# Initialize components
goal_manager = GoalManager(GOAL_FILE)
expense_tracker = ExpenseTracker(EXPENSE_FILE)
currency_converter = CurrencyConverter(EXCHANGE_RATE_FILE)

@app.route("/")
def home():
    return "Welcome to the Saving Goal Tracker!"

if __name__ == "__main__":
    app.run(debug=True)
