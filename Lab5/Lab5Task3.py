class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

student1 = Student("Dua", 20, [85, 90, 87, 92, 88])

print("Name:", student1.name)
print("Age:", student1.age)
print("Average Grade:", student1.average_grade())