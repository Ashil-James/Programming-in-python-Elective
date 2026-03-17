class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Animal __init__ called for {self.name}")

    def breathe(self):
        print(f"{self.name} is breathing")


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)   # calls Animal.__init__
        self.breed = breed
        print(f"Dog __init__ called for {self.name}")

    def bark(self):
        print(f"{self.name} says Woof!")


class GoldenRetriever(Dog):
    def __init__(self, name, age, breed, color):
        super().__init__(name, age, breed)   # calls Dog.__init__
        self.color = color
        print(f"GoldenRetriever __init__ called for {self.name}")

    def fetch(self):
        self.bark()
        super().bark()
        print(f"{self.name} the {self.color} {self.breed} is fetching!")


g = GoldenRetriever("Buddy", 3, "Golden Retriever", "golden")
g.fetch()
