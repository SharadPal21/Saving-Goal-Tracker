from flask import Flask, render_template, request, jsonify
from utils.goal_manager import GoalManager
from utils.expense_tracker import ExpenseTracker
from utils.currency_converter import CurrencyConverter
from utils.visualizer import Visualizer
import os

app = Flask(__name__)

# File paths
GOAL_FILE = "data/goals.json"
EXPENSE_FILE = "data/expenses.json"
EXCHANGE_RATE_FILE = "data/exchange_rates.json"

# Initialize utilities
goal_manager = GoalManager(GOAL_FILE)
expense_tracker = ExpenseTracker(EXPENSE_FILE)
currency_converter = CurrencyConverter(EXCHANGE_RATE_FILE)
visualizer = Visualizer(GOAL_FILE, EXPENSE_FILE)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/goals", methods=["GET", "POST"])
def goals():
    if request.method == "POST":
        goal = request.json.get("goal")
        goal_manager.add_goal(goal)
        return jsonify({"message": "Goal added successfully!"})
    return jsonify(goal_manager.get_goals())

@app.route("/expenses", methods=["GET", "POST"])
def expenses():
    if request.method == "POST":
        data = request.json
        expense_tracker.add_expense(data["amount"], data["category"])
        return jsonify({"message": "Expense added successfully!"})
    return jsonify(expense_tracker.get_expenses())

@app.route("/convert", methods=["POST"])
def convert_currency():
    data = request.json
    try:
        converted_amount = currency_converter.convert(data["amount"], data["from"], data["to"])
        return jsonify({"converted_amount": converted_amount})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@app.route("/visualize")
def visualize_data():
    visualizer.plot_goal_vs_expenses()
    return "Visualization generated."

if __name__ == "__main__":
    app.run(debug=True)
