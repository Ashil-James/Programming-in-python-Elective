class Father:
    def __init__(self, surname, height, **kwargs):
        super().__init__(**kwargs)   # passes remaining args up the chain
        self.surname = surname
        self.height = height
        print("Father __init__ called")


class Mother:
    def __init__(self, eye_color, **kwargs):
        super().__init__(**kwargs)   # passes remaining args up the chain
        self.eye_color = eye_color
        print("Mother __init__ called")


class Child(Father, Mother):
    def __init__(self, surname, height, eye_color, name):
        super().__init__(surname=surname, height=height, eye_color=eye_color)
        self.name = name
        print("Child __init__ called")


c = Child("Smith", 180, "blue", "Ash")