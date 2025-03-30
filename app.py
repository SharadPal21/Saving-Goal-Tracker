from flask import Flask, render_template, request, jsonify
from utils.chatbot_ai import ChatbotAI
from utils.goal_manager import GoalManager

app = Flask(__name__)

goal_manager = GoalManager("data/goals.json")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        user_input = request.json.get("message", "")
        response = ChatbotAI.get_response(user_input)
        return jsonify({"response": response})
    return render_template("chat.html")

@app.route("/goals", methods=["GET", "POST"])
def goals():
    if request.method == "POST":
        new_goal = request.form.get("goal")
        goal_manager.add_goal(new_goal)
    return render_template("goal_form.html", goals=goal_manager.get_goals())

if __name__ == "__main__":
    app.run(debug=True)
