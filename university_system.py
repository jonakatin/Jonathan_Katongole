class Person:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number

    def display_info(self):
        print(f"Name: {self.name}, ID: {self.id_number}")

class Student(Person):
    def __init__(self, name, id_number, course):
        super().__init__(name, id_number)
        self.course = course

    def display_info(self):
        super().display_info()
        print(f"Course: {self.course}")

class Lecturer(Person):
    def __init__(self, name, id_number, department):
        super().__init__(name, id_number)
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")

class Staff(Person):
    def __init__(self, name, id_number, role):
        super().__init__(name, id_number)
        self.role = role

    def display_info(self):
        super().display_info()
        print(f"Role: {self.role}")

student = Student("Alice", "S123", "Computer Science")
lecturer = Lecturer("Dr. Bob", "L456", "Engineering")
staff = Staff("Carol", "T789", "Administrator")

student.display_info()
print("----")
lecturer.display_info()
print("----")
staff.display_info()
