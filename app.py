from flask import Flask, request, jsonify, render_template
from utils.chatbot_ai import get_ai_response  # Import chatbot logic

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")  # Main dashboard

@app.route('/chatbot')
def chatbot():
    return render_template("chat.html")  # Chat UI

@app.route('/api/chat', methods=['POST'])
def chat():
    """Handles chat API requests."""
    data = request.get_json()
    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({"error": "Message cannot be empty"}), 400

    ai_response = get_ai_response(user_message)
    return jsonify({"response": ai_response})

if __name__ == "__main__":
    app.run(debug=True)
