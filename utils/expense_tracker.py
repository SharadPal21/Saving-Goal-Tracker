import json
import os

class ExpenseTracker:
    def __init__(self, file_path):
        self.file_path = file_path
        if not os.path.exists(file_path):
            with open(file_path, "w") as file:
                json.dump([], file)

    def add_expense(self, amount, category):
        expenses = self.get_expenses()
        expenses.append({"amount": amount, "category": category})
        self._save_expenses(expenses)

    def get_expenses(self):
        with open(self.file_path, "r") as file:
            return json.load(file)

    def _save_expenses(self, expenses):
        with open(self.file_path, "w") as file:
            json.dump(expenses, file, indent=4)
