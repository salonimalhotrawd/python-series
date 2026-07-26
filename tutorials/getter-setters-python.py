# @Program: Getter & Setters in Python
# @Author: Saloni Malhotra
# @Date: 26-07-2026

"""
A getter is a method used to read or retrieve the value of an object's attribute.
Instead of accessing the variable directly, we use a getter to get its value.


A setter is a method used to update or modify the value of an object's attribute.
A setter is useful because it can validate the new value before storing it.

"""

# 1st Program => Getter & Setter
# _________________________________________________________


class Employee:

    def __init__(self, salary):
        print("\nConstructor Initialization")
        print("=" * 35)
        self._salary = salary

    # Getter Method -> starts with @property
    @property
    def salary(self):
        return print(f"Employee Salary is: {self._salary}")

    # Setter Method -> starts with getter fxn Name @fxn.setter
    @salary.setter
    def set_salary(self, amount):
        if amount < 0:
            print("Salary cannot be negative")
            return False

        self._salary = amount
        return True


# 1st Employee
# ____________________________________
firstEmp = Employee(5000)
firstEmp.salary = 10000
firstEmp.salary

# 2nd Employee
# _____________________________________
secondEmp = Employee(8000)
secondEmp.salary = -100
secondEmp.salary
