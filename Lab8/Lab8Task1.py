import random

class VacuumEnvironment:
    def __init__(self):
        self.rooms = {"A": random.randint(0, 1),
                      "B": random.randint(0, 1),
                      "C": random.randint(0, 1),
                      "D": random.randint(0, 1)}

    def display_state(self, message):
        print(message)
        for room, state in self.rooms.items():
            print(f"Room {room}: {'Dirty' if state == 1 else 'Clean'}")

    def clean(self, room):
        if self.rooms[room] == 1:
            print(f"Cleaning {room}...")
            self.rooms[room] = 0
        else:
            print(f"{room} is already clean.")

    def run_agent(self):
        self.display_state("Initial State:")
        for room in self.rooms:
            self.clean(room)
        self.display_state("Final State:")

vacuum = VacuumEnvironment()
vacuum.run_agent()