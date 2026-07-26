# @Program: Access Modifiers in Python
# @Author: Saloni Malhotra
# @Date: 27-07-2026


"""
 ==================================
 ACCESS MODIFIERS IN PYTHON
 ==================================

1. Public    -> No underscore
    Example: self.name
    Accessible from anywhere.

2. Protected -> Single underscore (_)
    Example: self._salary
    Convention only; can still be accessed.

3. Private -> Double underscore (__)
    Example: self.__password
    Uses Name Mangling to discourage direct access.
    Internally becomes: self._ClassName__password

Note:
Python doesn't enforce access modifiers like Java/C++.
It relies on naming conventions.

"""

# 1st Program
# _______________________________________________________


class Employee:

    def __init__(self, name, salary, password):

        self.name = name  # Public
        self._salary = salary  # Protected
        self.__password = password  # Private


emp = Employee("Saloni", 5000000, "Saloni@1234")

print(emp.name)                   # ✅ Works
print(emp._salary)                # ✅ Works (but avoid)
# print(emp.__password)           # ❌ AttributeError

print(emp._Employee__password)    # ✅ Works (name mangling)
print(emp.__dir__())
