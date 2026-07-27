# @Program: operator overloading in Python
# @Author: Saloni Malhotra
# @Date: 27-07-2026

"""
Operator Overloading

Operator overloading allows us to define how Python operators (+, -, *, ==, >, <, etc.)
behave when used with objects of a custom class.

It is implemented using magic (dunder) methods like __add__, __sub__, __eq__, __gt__, etc.

Example:
emp1 + emp2
Internally becomes:
emp1.__add__(emp2)

Benefits:
- Makes code cleaner and more readable.
- Allows objects to behave like built-in data types.
- Useful for mathematical, financial, and domain-specific operations.
"""

# 1st Program
# ______________________________________________________________________


class Employee:

    def __init__(self, salary):
        self.salary = salary

    def __add__(self, other):
        return self.salary + other.salary


emp1 = Employee(120000)
emp2 = Employee(900000)

print(emp1 + emp2)


# 2nd Program
# ______________________________________________________________________


class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return (
            self.name.lower().strip() == other.name.lower().strip()
            and self.age == other.age
        )


studnt1 = Student("Saloni Malhotra", 31)
studnt2 = Student("SaloNi Malhotra", 31)

print(studnt1 == studnt2)


# 3rd Program
# ______________________________________________________________________


class Vector:

    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"

    def __add__(self, other):
        return Vector(self.i + other.i, self.j + other.j, self.k + other.k)


v1 = Vector(10, 20, 30)
v2 = Vector(40, 50, 60)

print(v1, "\n")
print(v2, "\n")
print(v1 + v2, "\n")
print(type(v1 + v2), "\n")
