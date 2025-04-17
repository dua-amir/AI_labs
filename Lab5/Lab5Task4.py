class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def display_details(self):
        print(f"Name: {self.name}, Salary: {self.salary}")
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
    def display_details(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Department: {self.department}")
class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language
    def display_details(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Programming Language: {self.programming_language}")
manager1 = Manager("Dua", 150000, "HR")
developer1 = Developer("Ayesha", 80000, "Python")
manager1.display_details()
developer1.display_details()
