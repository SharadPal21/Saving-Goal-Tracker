import openai
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

class ChatbotAI:
    def __init__(self):
        if not OPENAI_API_KEY:
            raise ValueError("Missing OpenAI API key. Add it to your .env file.")

    def get_response(self, user_input):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful financial advisor."},
                    {"role": "user", "content": user_input}
                ],
                max_tokens=100
            )
            return response["choices"][0]["message"]["content"]
        except Exception as e:
            return f"Error: {str(e)}"
