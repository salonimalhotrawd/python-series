# @Program: MultiLevel Inheritance in Python
# @Author: Saloni Malhotra
# @Date: 27-07-2026

"""
==========================================
        MULTILEVEL INHERITANCE
==========================================

Definition:
One class inherits from another class,
and another class inherits from that class.

GrandParent
     │
     ▼
  Parent
     │
     ▼
   Child

Example:
Person → Employee → Manager

Constructor Order:
Child → Parent → GrandParent

Method Search (MRO):
Child → Parent → GrandParent → object

Advantages:
✔ Code Reusability
✔ Less Code Duplication
✔ Easy to Extend

Disadvantages:
✘ Deep hierarchy is harder to understand
✘ Debugging becomes difficult

Key Points:
✔ Child inherits Parent and GrandParent members.
✔ Use super() to call the parent constructor.
✔ Python uses MRO to find methods.

==========================================

"""


class Person:

    def __init__(self, name):
        print("Person Constructor Called")
        self.name = name

    def show_name(self):
        print("Person show_name Called")
        print(f"Name : {self.name}")


class Employee(Person):

    def __init__(self, name, emp_id):
        print("Employee Constructor Called")
        super().__init__(name)

        self.emp_id = emp_id

    def show_name(self):
        super().show_name()
        print(f"Employee ID : {self.emp_id}")


class Manager(Employee):

    def __init__(self, name, emp_id, department):
        print("Manager Constructor Called")
        super().__init__(name, emp_id)

        self.department = department

    def show_name(self):
        super().show_name()
        print(f"Department ID : {self.emp_id}")

    def __str__(self):
        return f"{self.name} => {self.emp_id} => {self.department}"


# Object Creation
emp = Manager("Saloni Malhotra", 1, "IT")
print("=" * 40)
print(str(emp))
