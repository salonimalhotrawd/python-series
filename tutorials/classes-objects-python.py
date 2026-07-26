# @Program: Introduction to OOPS in Python
# @Author: Saloni Malhotra
# @Date: 26-07-2026

"""
    Procedural Programming (Function-Based Approach)

Procedural programming organizes a program into functions that perform specific tasks. Data is passed as arguments from one function to another whenever needed. It is simple, easy to understand, and well-suited for small programs or scripts. However, as applications grow, managing data across many functions can become difficult.

Object-Oriented Programming (Class-Based Approach)

Object-oriented programming (OOP) organizes code into classes and objects that combine both data (attributes) and behavior (methods). Each object stores its own information and can perform operations on that data. OOP makes code more organized, reusable, and easier to maintain, especially in large and complex applications.
"""

"""
    At first glance, the procedural (function-based) approach looks simpler because it requires less code and is easy to understand. It works well for small programs with limited functionality. However, as an application grows in size and complexity, managing data through multiple functions becomes difficult. In such cases, the object-oriented (class-based) approach is preferred because it organizes related data and functions together, making the code more reusable, maintainable, and scalable.
"""

"""
    self is a reference to the current object of a class. It allows an object to access its own variables (attributes) and methods. Whenever you create an object and call a method, Python automatically passes that object as the first argument to self. Although you can name it anything, self is the standard convention used in Python.
"""

# 1st Program in Procedural Approach
# ________________________________________________


def employeeForm(empployeeId, employeeName, employeeDesignation):
    return f"{employeeName} designation is {employeeDesignation} and its employee Id is {empployeeId}"


firstEmployee = employeeForm(1, "Saloni Malhotra", "Associate Product Lead")
secondEmployee = employeeForm(2, "Anmol Dogra", "Company Director & Chief")

print("\nFirst Employee Information is: ", firstEmployee, "\n")
print("Second Employee Information is: ", secondEmployee, "\n")


# 3rd Program Procedural Programming (Function Based) Approach
# ____________________________________________________________________

employees = [
    employeeForm(1, "Saloni Malhotra", "Associate Product Lead"),
    employeeForm(2, "Anmol Bharat Dogra", "Company Director & Chief"),
    employeeForm(3, "Rahul Sharma", "Software Engineer"),
    employeeForm(4, "Priya Verma", "HR Manager"),
    employeeForm(5, "Amit Kumar", "Senior Backend Developer"),
    employeeForm(6, "Neha Gupta", "UI/UX Designer"),
    employeeForm(7, "Rohit Singh", "QA Engineer"),
    employeeForm(8, "Sneha Kapoor", "Business Analyst"),
    employeeForm(9, "Vikash Das", "Technical Trainer"),
    employeeForm(10, "Riya Mehta", "Data Scientist"),
]

print("========== Function Based Approach ==========\n")

for i, employee in enumerate(employees, start=1):
    print(f"Employee {i}: {employee}")


# 3rd Program in Class Based Approach
# _____________________________________________________


class Employee:
    id = 1
    name = "Saloni Malhotra"
    designation = "Associate Product Lead"

    def employeeInfo(self):
        return f"{self.name} designation is {self.designation} and its employee Id is {self.id}"


firstClassEmployee = Employee()

secondClassEmployee = Employee()
secondClassEmployee.id = 2
secondClassEmployee.name = "Anmol Bharat Dogra"
secondClassEmployee.designation = "Company Director & Chief"

print(
    "\nFirst Employee Information in Class Based Approach is: ",
    firstClassEmployee.employeeInfo(),
    "\n",
)
print(
    "Second Employee Information in Class Based Approach is: ",
    secondClassEmployee.employeeInfo(),
    "\n",
)


# 4th Program Class Based Approach another Example
# _____________________________________________________

# Employee 1
emp1 = Employee()
emp1.id = 1
emp1.name = "Sansha Handa"
emp1.designation = "Associate Product Lead"

# Employee 2
emp2 = Employee()
emp2.id = 2
emp2.name = "Anmol Bharat Dogra"
emp2.designation = "Company Director & Chief"

# Employee 3
emp3 = Employee()
emp3.id = 3
emp3.name = "Rahul Sharma"
emp3.designation = "Software Engineer"

# Employee 4
emp4 = Employee()
emp4.id = 4
emp4.name = "Priya Verma"
emp4.designation = "HR Manager"

# Employee 5
emp5 = Employee()
emp5.id = 5
emp5.name = "Amit Kumar"
emp5.designation = "Senior Backend Developer"

# Employee 6
emp6 = Employee()
emp6.id = 6
emp6.name = "Neha Gupta"
emp6.designation = "UI/UX Designer"

# Employee 7
emp7 = Employee()
emp7.id = 7
emp7.name = "Rohit Singh"
emp7.designation = "QA Engineer"

# Employee 8
emp8 = Employee()
emp8.id = 8
emp8.name = "Sneha Kapoor"
emp8.designation = "Business Analyst"

# Employee 9
emp9 = Employee()
emp9.id = 9
emp9.name = "Vikash Das"
emp9.designation = "Technical Trainer"

# Employee 10
emp10 = Employee()
emp10.id = 10
emp10.name = "Riya Mehta"
emp10.designation = "Data Scientist"

employeeList = [emp1, emp2, emp3, emp4, emp5, emp6, emp7, emp8, emp9, emp10]

print("\n========== Class Based Approach ==========\n")

for employee in employeeList:
    print(employee.employeeInfo())
