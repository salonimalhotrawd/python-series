# @Program: Inheritance in Python
# @Author: Saloni Malhotra
# @Date: 26-07-2026


"""
Inheritance is a mechanism in which one class acquires the properties (variables) and behaviors (methods) of another class.
The class being inherited from is called the Parent (Base/Super) class, and the class that inherits is called the Child (Derived/Sub) class.

"""

# 1st Program Inheritance
# ____________________________________________________________________


class Animal:

    def __init__(self, type, name):
        print("\nAnimal Class Initialization")
        print("=" * 30)
        self._type = type
        self._name = name

    def showAnimalType(self):
        print(f"\n{self._type} Type is: {self._name}")


class Voice(Animal):

    def __init__(self, type, name, voice):
        print("\nVoice Class Initialization")
        super().__init__(type, name)
        self._voice = voice

    def playAnimalVoice(self):
        print(f"The {self._type} is doing {self._voice}")


# 1st Animal
dog = Animal("Animal", "Dog")
dog.showAnimalType()

# 2nd Animal
cat = Voice("Animal", "Cat", "Meow Meow")
cat.showAnimalType()
cat.playAnimalVoice()

# 3rd Animal
bird = Voice("Bird", "Crow", "Caw Caw")
bird.showAnimalType()
bird.playAnimalVoice()
