class Superhero:
    def __init__(self, name, superpower):
        self.name = name
        self.superpower = superpower

    def use_superpower(self):
        print(f"{self.name} uses {self.superpower}!")

#Create a superhero object
superman = Superhero("Superman", "super strength")

#Call the use_superpower() method
superman.use_superpower()