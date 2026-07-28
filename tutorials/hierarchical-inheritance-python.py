# @Program: Hierarchial Inheritance in Python
# @Author: Saloni Malhotra
# @Date: 28-07-2026


"""
 =============================================================================
              Hierarchical Inheritance - Quick Revision
 =============================================================================

 Syntax

 class Parent:
     pass


 class Child1(Parent):
     pass


 class Child2(Parent):
     pass


              Parent
             /      \
            /        \
        Child1     Child2

 Hierarchical Inheritance:
 • One Parent Class
 • Multiple Child Classes

 super()
 • Calls the parent class constructor/method.

 Syntax:
 super().__init__(arguments)

 Advantages:
 • Reuses parent code
 • Avoids duplicate initialization
 • Cleaner and recommended approach

 =============================================================================
"""

# 1st Program
# ______________________________________________________


class Employee:

    def __init__(self, name, emp_id):
        print("Employee Constructor Called")

        self.name = name
        self.emp_id = emp_id

    def display_details(self):
        print(f"Name        : {self.name}")
        print(f"Employee ID : {self.emp_id}")


class Developer(Employee):

    def __init__(self, name, emp_id, programming_language):

        super().__init__(name, emp_id)
        self.programming_language = programming_language

    def display_details(self):
        super().display_details()
        print(f"Programming Language : {self.programming_language}")

    def write_code(self):
        print(f"{self.name} writes code in {self.programming_language}")


class Tester(Employee):

    def __init__(self, name, emp_id, testing_tool):

        super().__init__(name, emp_id)
        self.testing_tool = testing_tool

    def display_details(self):
        super().display_details()
        print(f"Testing Tool : {self.testing_tool}")

    def test_application(self):
        print(f"{self.name} tests applications using {self.testing_tool}")


# Developer Object
developer = Developer("Saloni", 101, "Python")

print()

developer.display_details()
developer.write_code()

print("\n" + "-" * 40 + "\n")

# Tester Object
tester = Tester("Rahul", 102, "Selenium")

print()

tester.display_details()
tester.test_application()
