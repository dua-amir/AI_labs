class TrafficLightAgent:
    def act(self, light_color):
        actions = {"red": "Stop", "yellow": "Ready", "green": "Move"}
        return actions.get(light_color.lower(), "Invalid color")

traffic_agent = TrafficLightAgent()

for color in ["Red", "Yellow", "Green"]:
    print(f"Light: {color} → Action: {traffic_agent.act(color)}")
