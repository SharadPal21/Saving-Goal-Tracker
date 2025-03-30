import matplotlib.pyplot as plt
import json

class Visualizer:
    def __init__(self, goal_file, expense_file):
        self.goal_file = goal_file
        self.expense_file = expense_file

    def plot_goal_vs_expenses(self):
        with open(self.goal_file, "r") as file:
            goals = json.load(file)

        with open(self.expense_file, "r") as file:
            expenses = json.load(file)

        goal_values = [100] * len(goals)  # Assume each goal is 100% target
        expense_values = [sum([e["amount"] for e in expenses]) / len(goals)] * len(goals)

        plt.figure(figsize=(8, 4))
        plt.bar(goals, goal_values, color="green", label="Goal")
        plt.bar(goals, expense_values, color="red", label="Spent")
        plt.xlabel("Goals")
        plt.ylabel("Amount")
        plt.title("Goal vs. Expenses")
        plt.legend()
        plt.show()
