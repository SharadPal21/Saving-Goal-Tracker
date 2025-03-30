import os
import sys
from flask import Flask, render_template, request, jsonify
from utils.chatbot_ai import ChatbotAI

# Ensure utils is recognized as a package
sys.path.append(os.path.abspath("utils"))

app = Flask(__name__)

# Initialize Chatbot
chatbot = ChatbotAI()

# Home Route
@app.route("/")
def home():
    return render_template("index.html")

# Chat Page Route
@app.route("/chat")
def chat():
    return render_template("chat.html")

# Chatbot API Route
@app.route("/api/chat", methods=["POST"])
def chat_with_ai():
    try:
        data = request.get_json()
        user_message = data.get("message", "").strip()

        if not user_message:
            return jsonify({"error": "Message cannot be empty"}), 400
        
        bot_response = chatbot.get_response(user_message)
        return jsonify({"response": bot_response})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Expense Tracker API Route (Placeholder)
@app.route("/expenses", methods=["GET"])
def get_expenses():
    return jsonify({"message": "Expense tracking API will be implemented soon"}), 200

# Start Flask App
if __name__ == "__main__":
    app.run(debug=True)
