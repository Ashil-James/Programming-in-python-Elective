class Animal:
    def speak(self):
        print("Play some sound...")
    
class Dog(Animal):
    def speak(self):
        print("Woof")

class Cat(Animal):
    def speak(self):
        print("Meow")
        
animals = [Dog(), Cat(), Animal()]
for a in animals:
    a.speak()