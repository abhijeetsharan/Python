class Person:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Name:", self.name)

# Child class (inherits from person)
class Student(Person):
    def __init__(self, name, course):
        super().__init__(name) # call parent constructor
        self.course = course

    def show_details(self):
        print(f"Name: {self.name}, Course: {self.course}")

