class Student:
    def __init__(self, roll_number, name):
        self.roll_number = roll_number
        self.name = name
    def details(self):
        print(f"Roll Number: {self.roll_number}, Name: {self.name}")
student1 = Student(46462, "Zainab")
student2 = Student(46484, "Samreen")
print("Before updating:")
student1.details()
student2.details()
student1.name = "Dua"
student2.roll_number = 47849
print("After updating:")
student1.details()
student2.details()
