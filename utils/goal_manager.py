import json
import os

class GoalManager:
    def __init__(self, file_path):
        self.file_path = file_path
        if not os.path.exists(file_path):
            with open(file_path, "w") as file:
                json.dump([], file)

    def add_goal(self, goal):
        goals = self.get_goals()
        goals.append(goal)
        self._save_goals(goals)

    def get_goals(self):
        with open(self.file_path, "r") as file:
            return json.load(file)

    def _save_goals(self, goals):
        with open(self.file_path, "w") as file:
            json.dump(goals, file, indent=4)
