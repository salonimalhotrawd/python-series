# @Program: Single Inheritance in Python
# @Author: Saloni Malhotra
# @Date: 27-07-2026

"""
Single Inheritance:
One child class inherits the properties and methods of one parent class.

Benefits:
- Reuses existing code.
- Child can access parent methods and variables.
- Child can add its own functionality.
- Supports method overriding for customization.
"""

# 1st Program
# _________________________________________________________


class Animal:

    def __init__(self, name, species):

        print("Animal Class Constructor Initialization")

        self.name = name
        self.species = species

    def make_sound(self):
        print("Animal Making Sound \n")

    def print_species_name(self):
        print("Printing Species name")


class Dog(Animal):

    def __init__(self, name, species, breed):

        print("Dog Class Constructor Initialization")

        super().__init__(name, species)
        self.breed = breed

    def make_sound(self):
        print("Bow Bow \n")

    def print_species_name(self):
        super().print_species_name()  # Method overriding
        print(f"The Breed is: {self.breed}")


bird = Animal("Jimmy", "Pet")

print("=" * 50)
bird.make_sound()
print("=" * 50)

print("=" * 50)
dog = Dog("Lisa", "Dog", "Pet")
dog.make_sound()
dog.print_species_name()
print("=" * 50)
