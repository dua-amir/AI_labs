class AutomaticDoor:
    def __init__(self):
        self.night_mode = False
    def detect_person(self, person_detected, authorized=False):
        if self.night_mode and not authorized:
            return "Door remains closed (Security Mode)"
        return "Door opens" if person_detected else "Door closes"

door = AutomaticDoor()
print(door.detect_person(True))  # Door opens
print(door.detect_person(False))  # Door closes

door.night_mode = True
print(door.detect_person(True, authorized=False))  # Door remains closed
print(door.detect_person(True, authorized=True))   # Door opens
