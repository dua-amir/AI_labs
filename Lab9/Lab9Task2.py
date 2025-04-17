# 🎯 Goal-Based Agent: Tries to reach a target position step by step
class GoalBasedAgent:

    # 🏁 Constructor to set starting and goal positions
    def __init__(self, start, goal):
        self.position = start  # Starting coordinates (x, y)
        self.goal = goal  # Goal coordinates (gx, gy)

    # 🚶‍♀️ Action method that moves the agent toward the goal
    def act(self):
        x, y = self.position  # Current position
        gx, gy = self.goal  # Goal position

        # ➡️ Move one step toward the goal in x-direction first
        if x < gx:
            self.position = (x + 1, y)
        # ⬇️ If x is aligned, move in y-direction
        elif y < gy:
            self.position = (x, y + 1)

        # 🖨️ Show the agent’s new position
        print(f"Goal-Based: Moved to {self.position}")


# 🧠 Model-Based Agent: Makes decisions using internal memory (model of the environment)
class ModelBasedAgent:

    # 📦 Constructor initializes the model — assumes the room starts as 'Dirty'
    def __init__(self):
        self.model = {'Room': 'Dirty'}  # Memory of the world state

    # 🤖 Action method performs based on what the model remembers
    def act(self):
        # 🧹 If room is dirty, clean it and update memory
        if self.model['Room'] == 'Dirty':
            print("Model-Based: Cleaning room.")
            self.model['Room'] = 'Clean'
        # 🛋️ If already clean, no action needed
        else:
            print("Model-Based: Nothing to do.")


# ⚖️ Utility-Based Agent: Chooses the task with the highest reward (utility)
class UtilityBasedAgent:

    # 📊 Constructor defines available tasks and their respective utility values
    def __init__(self):
        self.choices = {'Eat': 5, 'Sleep': 3, 'Code': 10}  # Tasks with utility scores

    # 🏆 Action method selects the task with the highest utility
    def act(self):
        best_action = max(self.choices, key=self.choices.get)  # Find the task with max utility
        print(f"Utility-Based: Chose to {best_action} with utility {self.choices[best_action]}")  # Show choice


# 🚀 Run all three agents and demonstrate their behaviors

# 🎯 Initialize goal-based agent with start at (0,0) and goal at (2,2)
goal_agent = GoalBasedAgent(start=(0, 0), goal=(2, 2))

# 🧠 Initialize the model-based agent
model_agent = ModelBasedAgent()

# ⚖️ Initialize the utility-based agent
utility_agent = UtilityBasedAgent()

# ✨ Separator for clarity in output
print("\n--- Agents in Action ---")

# 👣 Move the goal-based agent 3 times toward the goal
for _ in range(3):
    goal_agent.act()

# 🧹 Model-based agent cleans once, then checks again
model_agent.act()  # Cleans the room
model_agent.act()  # Checks and finds nothing to do

# 🏆 Utility-based agent selects the task with highest reward
utility_agent.act()
