# @Program: Static Methods in Python
# @Author: Saloni Malhotra
# @Date: 26-07-2026


"""
    ==================================
        STATIC METHODS IN PYTHON
    ==================================

    A static method is a method that belongs to a class but does not use
    instance variables (self) or class variables (cls).

    It is created using the @static method decorator.

    Static methods are mainly used for utility or helper functions that are
    related to the class but do not need to access or modify the object's or
    class's data.

    A static method can be called using:
    1. ClassName.method_name()
    2. object_name.method_name()

    Example:
        Calculator.add(10, 20)
Note:
A static method doesn't exist because Python can't use normal functions. It exists to keep related utility functions organized inside a class.

"""

# 1st Program
# ________________________________________________________________________


class Calculator:

    def __init__(self):
        print("Calculator Class Constructor Initilization")

    @staticmethod
    def additionOfTwoNums(a, b):
        return a + b

    @staticmethod
    def multiplicationOfTwoNums(a, b):
        return a * b


calc = Calculator()
print(calc.additionOfTwoNums(10, 30))
print(Calculator.multiplicationOfTwoNums(20, 40))


# 2nd Program
# ________________________________________________________________________________


class Employee:

    def __init__(self, name, salary):
        print("\nEmployee Class Constructor Initilization")

        self.name = name
        self.salary = salary

    @staticmethod
    def is_valid_email(email):
        return "@" in email

    @staticmethod
    def is_eligible_age(age):
        return age >= 18

    @staticmethod
    def is_valid_employee_id(emp_id):
        return emp_id.startswith("EMP-")


# Note: If we dont create any Employee Class then constructor method will not call
emp1 = Employee("Saloni Malhotra", 500000)
print(Employee.is_eligible_age(5))

# Directly call the static Method without creating any class Employee
print(Employee.is_valid_email("saloni12@gmail.com"))
print(Employee.is_eligible_age(25))
print(Employee.is_valid_employee_id("EMP-101"))
