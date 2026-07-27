# @Program: magic/Dunder Methods in Python
# @Author: Saloni Malhotra
# @Date: 27-07-2026


"""
    Magic (Dunder) Methods Example
    ------------------------------
    This program demonstrates some commonly used magic methods:
    __init__()    -> Called automatically when an object is created.
    __str__()     -> Returns a user-friendly string representation.
    __repr__()    -> Returns an official string representation, mainly for debugging.
    __len__()     -> Enables the use of len(object).
    __add__()     -> Defines behavior for the + operator.
    __eq__()      -> Defines behavior for the == operator.
    __lt__()      -> Defines behavior for the < operator.
    __getitem__() -> Enables indexing like object[index].
    __call__()    -> Allows an object to be called like a function.
    
"""
# 1st Program
# ___________________________________________________


class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.skills = ["Python", "React", "Angular"]

    # Called by print(object)
    def __str__(self):
        return f"Employee(Name='{self.name}', Salary=${self.salary})"

    # Called by repr(object) or in debugging
    def __repr__(self):
        return f" Employee('{self.name}', {self.salary})"

    # Called by len(object)
    def __len__(self):
        return len(self.skills)

    # Called by object1 + object2
    def __add__(self, other):
        return self.salary + other.salary

    # Called by object1 == object2
    def __eq__(self, other):
        return self.salary == other.salary

    # Called by object1 < object2
    def __lt__(self, other):
        return self.salary < other.salary

    # Called by object[index]
    def __getitem__(self, index):
        return self.skills[index]

    # Called by object()
    def __call__(self):
        print(f"Hello! I am {self.name}.")


emp1 = Employee("Saloni", 90000)
emp2 = Employee("Rohit", 80000)

print("----- __str__ -----")
print(emp1)

print("\n----- __repr__ -----")
print(repr(emp1))

print("\n----- __len__ -----")
print(len(emp1))

print("\n----- __add__ -----")
print(emp1 + emp2)

print("\n----- __eq__ -----")
print(emp1 == emp2)

print("\n----- __lt__ -----")
print(emp1 < emp2)

print("\n----- __getitem__ -----")
print(emp1[0])
print(emp1[1])

print("\n----- __call__ -----")
emp1()
