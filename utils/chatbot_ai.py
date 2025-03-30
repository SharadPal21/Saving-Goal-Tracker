import random

class ChatbotAI:
    responses = {
        "hello": ["Hi there!", "Hello!", "Hey! How can I help you?"],
        "goal": ["Tracking your goals is a great habit!", "I can help you set and monitor your savings goals."],
        "expense": ["Keeping track of expenses helps with budgeting.", "I can log your expenses and show insights."],
        "bye": ["Goodbye! Have a great day!", "See you later!"]
    }

    @staticmethod
    def get_response(user_input):
        user_input = user_input.lower()
        for key in ChatbotAI.responses:
            if key in user_input:
                return random.choice(ChatbotAI.responses[key])
        return "I'm not sure how to respond. Can you ask something else?"
