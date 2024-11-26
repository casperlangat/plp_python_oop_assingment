class Animal:
    def move(self):
        raise NotImplementedError("Subclass must implement move()")
    
class Cat(Animal):
    def move(self):
        print("Cat walk on four legs")

class Dog(Animal):
    def move(self):
        print("Dog run on four legs")

class Bird(Animal):
    def move(self):
        print("Bird fly in the sky")

# Create a list of animals
animal = [Cat(), Dog(), Bird()]

# Call the move() method for each animal
for animal in animal:
    animal.move()