class Person:
    def __init__(self, name, age):
        print("Person constructor called")
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

    def greet(self):
        print("Hello from Person class")


class Student(Person):   # Inheriting from Person
    def __init__(self, name, age, roll_no):
        print("Student constructor called")

        # Calling parent constructor using super()
        super().__init__(name, age)

        self.roll_no = roll_no

    def display_student(self):
        # Accessing parent data members
        print(f"Name: {self.name}")   # from Person
        print(f"Age: {self.age}")     # from Person
        print(f"Roll No: {self.roll_no}")

    def greet(self):
        print("Hello from Student class")

        # Calling parent method using super()
        super().greet()