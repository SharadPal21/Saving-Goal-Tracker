import random

class ChatbotAI:
    def __init__(self):
        self.default_response = "I'm here to help. Ask me anything about saving goals!"
        
        # Define chatbot responses
        self.responses = {
            "hello": ["Hello! How can I assist you with your savings?", "Hi there! Need help with financial goals?"],
            "how are you": ["I'm just a bot, but I'm here to help you!", "I'm good! Ready to assist with your savings!"],
            "bye": ["Goodbye! Have a great day managing your savings!", "See you later! Keep saving wisely!"],
            "how to save money": [
                "Start by tracking expenses and setting a budget.",
                "Try the 50/30/20 rule: 50% needs, 30% wants, 20% savings.",
                "Cut down unnecessary expenses and set financial goals!"
            ],
            "best way to invest": [
                "Consider low-risk investments like fixed deposits or mutual funds.",
                "Diversify your portfolio to balance risks and rewards.",
                "Research and consult a financial advisor before investing."
            ]
        }

    def get_response(self, message):
        """Returns a chatbot response based on user input."""
        message = message.lower().strip()
        return random.choice(self.responses.get(message, [self.default_response]))
