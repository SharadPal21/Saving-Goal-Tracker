from flask import Flask, render_template, request, jsonify
import os
import logging
from utils.expense_tracker import ExpenseTracker
from utils.currency_converter import CurrencyConverter
from utils.goal_manager import GoalManager
from utils.chatbot_ai import ChatbotAI

app = Flask(__name__)

# Initialize logging
logging.basicConfig(filename='logs/app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize utilities
expense_tracker = ExpenseTracker("data/expenses.json")
goal_manager = GoalManager("data/goals.json")
currency_converter = CurrencyConverter("data/exchange_rates.json")
chatbot = ChatbotAI()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        user_message = request.json.get('message', '')
        response = chatbot.get_response(user_message)
        return jsonify({"response": response})
    return render_template('chat.html')

@app.route('/goals', methods=['GET', 'POST'])
def goals():
    if request.method == 'POST':
        goal_data = request.json
        goal_manager.add_goal(goal_data)
        return jsonify({"message": "Goal added successfully"})
    return render_template('goal_form.html')

@app.route('/expenses', methods=['GET', 'POST'])
def expenses():
    if request.method == 'POST':
        expense_data = request.json
        expense_tracker.add_expense(expense_data)
        return jsonify({"message": "Expense added successfully"})
    return jsonify(expense_tracker.get_expenses())

@app.route('/convert-currency', methods=['POST'])
def convert_currency():
    data = request.json
    amount = data.get("amount")
    from_currency = data.get("from_currency")
    to_currency = data.get("to_currency")
    
    converted_amount = currency_converter.convert(amount, from_currency, to_currency)
    return jsonify({"converted_amount": converted_amount})

if __name__ == '__main__':
    app.run(debug=True)
