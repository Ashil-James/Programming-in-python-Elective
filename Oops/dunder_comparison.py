class Student:
    def __init__(self, marks):
        self.marks = marks

    def __eq__(self, other):
        return self.marks == other.marks

    def __lt__(self, other):
        return self.marks < other.marks

# Usage
s1 = Student(85)
s2 = Student(90)

print(s1 == s2)
print(s1 < s2)