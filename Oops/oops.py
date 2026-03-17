class Dog:
    species = "Canis lupus"

    def __init__(self, name):
        self.name = name

    def show_species(self):
        print(self.species)   # reads from object first, then class

dog1 = Dog("Buddy")
dog2 = Dog("Max")

# Override species on dog1 only
dog1.species = "Mutant Dog"  # creates an instance attribute on dog1

dog1.show_species()   # Mutant Dog  ← reads dog1's own species
dog2.show_species()   # Canis lupus ← falls back to class attribute