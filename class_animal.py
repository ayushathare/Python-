class Animal:
    def __init__(self, species, sound):
        self.species = species
        self.sound = sound

    def make_sound(self):
        print(f"The {self.species} says {self.sound}!")


animal1 = Animal("Dog", "Woof")
animal1.make_sound()

animal2 = Animal("Cat", "Meow")
animal2.make_sound()
