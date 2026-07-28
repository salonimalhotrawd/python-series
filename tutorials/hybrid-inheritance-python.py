# @Program: Hybrid Inheritance in Python
# @Author: Saloni Malhotra
# @Date: 28-07-2026

"""
 ============================================================
                HYBRID INHERITANCE (Quick Revision)
 ============================================================

 Definition
 ----------
 Hybrid Inheritance = Combination of two or more types of inheritance.

 Examples:
 - Single + Multiple
 - Hierarchical + Multiple
 - Multilevel + Multiple


 Common Structure
 ----------------

           A
          / \
         B   C
          \ /
           D

 A -> Base Class
 B, C -> Child Classes
 D -> Inherits from B and C

 Hierarchical + Multiple = Hybrid Inheritance


 Why use?
 --------
 ✔ Code Reusability
 ✔ Reduce Duplicate Code
 ✔ Flexible Class Design


 MRO
 ---
 Method Resolution Order (MRO) decides the order
 in which Python searches methods and constructors.

 Check using:
 ClassName.mro()


 Syntax
 ------

 class A:
     ...

 class B(A):
     ...

 class C(A):
     ...

 class D(B, C):
     ...

 obj = D()

"""

# 1st Program => Hybrid Inheritance
# ____________________________________________________


class Person:

    def __init__(self, name, **kwargs):
        print("Person Constructor")

        self.name = name
        super().__init__(**kwargs)

    def show_name(self):
        print(f"Name : {self.name}")


class Employee(Person):

    def __init__(self, employee_id, **kwargs):
        print("Employee Constructor")

        self.employee_id = employee_id
        super().__init__(**kwargs)

    def show_employee(self):
        print(f"Employee ID : {self.employee_id}")


class Student(Person):

    def __init__(self, course, **kwargs):
        print("Student Constructor")

        self.course = course
        super().__init__(**kwargs)

    def show_course(self):
        print(f"Course : {self.course}")


class Intern(Employee, Student):

    def __init__(self, name, employee_id, course):
        print("Intern Constructor")

        super().__init__(name=name, employee_id=employee_id, course=course)

    def display(self):
        self.show_name()
        self.show_employee()
        self.show_course()


intern = Intern(name="Saloni", employee_id=101, course="Python")

print()

intern.display()

print()

print("MRO:")
print(Intern.mro())
