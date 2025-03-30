from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import os
import openai

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Ensure API key is set
if not OPENAI_API_KEY:
    raise ValueError("Missing OpenAI API Key in environment variables")

openai.api_key = OPENAI_API_KEY  # Set OpenAI API key

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")

    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # or "gpt-3.5-turbo"
            messages=[
                {"role": "system", "content": "You are a financial advisor."},
                {"role": "user", "content": user_message}
            ],
            max_tokens=150
        )
        reply = response.choices[0].message.content  # Corrected way to access response
        return jsonify({"reply": reply})
    except openai.error.OpenAIError as e:
        return jsonify({"error": f"OpenAI API Error: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": f"Server Error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)  # Set to False in production
