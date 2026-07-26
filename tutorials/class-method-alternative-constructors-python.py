# @Program: Class Method Alternative Constructors in Python
# @Author: Saloni Malhotra
# @Date: 27-07-2026


"""

Alternate Constructor
---------------------
    1) A class method that provides another way to create objects.

    2) It is useful when object data comes in a different format,
    such as a string, CSV file, database record, or API response.
    and then creates the object using cls(...).

    3) Using cls() supports inheritance by creating objects of
    the calling class instead of a hardcoded class.

    Why use cls() instead of the class name?
        - Supports inheritance.
        - Creates an object of the class from which the method is called.

"""

# 1st Program
# ___________________________________________________________


class Employee:

    def __init__(self, name, salary):
        print("\nEmployee Class Constructor Initialization")
        print("=" * 60)

        self.name = name
        self.salary = salary

    def showEmployeeDetails(self):
        print(f"\nEmployee Name is: {self.name} and the Salary is {self.salary}\n")

    @classmethod
    def fromStr(cls, string):
        return cls(string.split("-")[0], int(string.split("-")[1]))

    @classmethod
    def fromUnderscore(cls, string):
        return cls(string.split("_")[0], int(string.split("_")[1]))


# 1st Employee
emp1 = Employee("Saloni Malhotra", 12000)
emp1.showEmployeeDetails()

# 2nd Employee
str = "Krishna Sharma-30000"
emp2 = Employee.fromStr(str)
emp2.showEmployeeDetails()

# 2nd Employee
str1 = "Rohit Shetty_90000"
emp3 = Employee.fromUnderscore(str1)
emp3.showEmployeeDetails()
