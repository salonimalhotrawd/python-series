# @Program: Method Overriding in Python
# @Author: Saloni Malhotra
# @Date: 27-07-2026

"""
Method Overriding is an OOP feature where a child class provides its own implementation of a method that is already defined in its parent class. When the method is called on the child object, Python executes the child class's version instead of the parent's.
"""

# 1st Program
# ____________________________________________________________


class Animal:
    def sound(self):
        print("Animals make different sounds")


class Dog(Animal):
    def sound(self):
        print("Dog barks")


dog = Dog()
dog.sound()


# 2nd Program -> Employee Salary
# ____________________________________________________________


class Employee:
    def calculate_salary(self):
        print("Basic salary calculation")


class Manager(Employee):
    def calculate_salary(self):
        print("Salary = Basic + Bonus")


manager = Manager()
manager.calculate_salary()
