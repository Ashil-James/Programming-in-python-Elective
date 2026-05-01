from abc import ABC, abstractmethod

# Abstract Class
class Person(ABC):
    def __init__(self, name):
        self.name = name
        print("Person constructor called")

    @abstractmethod
    def show_role(self):
        pass


# Child Class
class Student(Person):
    def __init__(self, name, roll_no):
        super().__init__(name)   # calling parent constructor
        self.roll_no = roll_no
        print("Student constructor called")

    def show_role(self):   # implementing abstract method
        print(f"{self.name} is a Student with roll no {self.roll_no}")


# Another Child Class
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
        print("Teacher constructor called")

    def show_role(self):
        print(f"{self.name} teaches {self.subject}")


# Creating objects
s = Student("John", 101)
t = Teacher("Alice", "Math")

# Calling methods
s.show_role()
t.show_role()