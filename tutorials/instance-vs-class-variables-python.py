# @Program: Access Modifiers in Python
# @Author: Saloni Malhotra
# @Date: 27-07-2026

"""
    ==========================================================
    Purpose of Instance Variables:
    ----------------------------------------------------------

    Instance variables store data that is unique to each object.
    Every object has its own separate copy of these variables.
        Examples:
            - name
            - salary
            - age
    ==========================================================


    ==========================================================
        Purpose of Class Variables:
    ----------------------------------------------------------
    Class variables store data that is common to all objects.
    A single copy is shared by every instance of the class.
        Examples:
            - company name
            - school name
            - tax rate
    ==========================================================

Rule to Remember
==========================================================
   Python looks for an attribute in this order:
    1. Instance variables (object)
    2. Class variables (class)

"""

# 1st Program
# ______________________________________________________________

class Employee:
    companyName = "Apple"
    companySize = 0
    
    def __init__(self, name):
        print("\nEmployee Class Constructor Initilization")
        print("=" * 45)
        
        self.name = name
        self._raise_amount = 2 # Private
        Employee.companySize += 1
        
        
    def showEmployeeDetails(self):
        print(f"\nEmployee Name is: {self.name} and the Company Name is {self.companyName} and its size is {self.companySize} \n")
        
   
# 1st Employee     
emp1 = Employee("Saloni Malhotra")
emp1.showEmployeeDetails()


# 2nd Employee     
emp2 = Employee("Shweta Srivastava")
emp2.companyName = "Microsoft"
emp2.showEmployeeDetails()

Employee.companyName = "Google"
print(f"\n {Employee.companyName}")

# 3rd Employee
emp3 = Employee("Shreya Kalra")
emp3.showEmployeeDetails()
    
        
        
