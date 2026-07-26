#  @Program: Class Methods in Python
#  @Author: Saloni Malhotra
#  @Date: 27-07-2026

"""
   ==========================================================
      Class Methods in Python
   ----------------------------------------------------------
   A class method is a method that works with the class itself,
   not with individual objects.

   It is created using the @classmethod decorator.

   The first parameter is 'cls', which refers to the class.

   Class methods are mainly used to:
   1. Access class variables.
   2. Modify class variables.
   3. Create alternative constructors (factory methods).

Syntax:

class ClassName:

    @classmethod
    def method_name(cls):
         code
==========================================================

"""


class Employee:

    companyName = "Microsoft"

    def __init__(self, name):
        print("\nEmployee Class Constructor Initilization")
        print("=" * 45)

        self.name = name

    def showEmployeeInfo(self):
        print(
            f"\nEmployee Name is: {self.name} and the Company Name is {self.companyName} \n"
        )

    @classmethod
    def changeCompanyName(cls, new_company_name):
        cls.companyName = new_company_name


# 1st Employee
emp1 = Employee("Saloni Malhotra")
Employee.showEmployeeInfo(emp1)


Employee.changeCompanyName("Google")
print(f"\n The New Company Name is: {Employee.companyName}")

# 2nd Employee
emp2 = Employee("Anmol Dogra")
emp2.showEmployeeInfo()
