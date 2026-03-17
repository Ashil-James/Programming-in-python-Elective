class Student:
    def __init__(self, name, marks):
        self.__name = name
        self.__marks = marks
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if type(value) != str:
            print("Name must be a string!")
        else:
            self.__name = value

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, value):
        if value < 0 or value > 100:
            print("Invalid marks!")
        else:
            self.__marks = value


student = Student("Ash", 85)
print(student.name)     # Ash
student.name = "Ashil"   # ✅
print(student.name)
student.marks = 95     # Invalid!
print(student.marks)