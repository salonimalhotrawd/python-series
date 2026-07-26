# @Program: Constructors in Python
# @Author: Saloni Malhotra
# @Date: 26-07-2026


"""
A constructor is a special method in a class that is automatically called when an object is created. It is used to initialize (assign) values to an object's attributes. In Python, the constructor is written as __init__(). This helps create objects with different values without assigning each attribute separately.
"""

# 1st Program Constructor
# __________________________________________________________________

class Employee:
    
    # Paramterized Constructor
    def __init__(self):
        print("Default Constructor is Initialized", self)
    
 
firstEmployee = Employee()


# 2nd Program -> Parameterized Constructor
# _________________________________________________________________

class Student:
    
    # Paramterized Constructor
    def __init__(self,rollNo,name):
        print("Default Constructor is Initialized")
        self.rollNo = rollNo
        self.name = name
    
    def studentInfo(self):
        print(f"Student Name is {self.name} and its roll Number is {self.rollNo}")
        

firstStudent = Student("Saloni Malhotra", 1)
print(firstStudent.studentInfo())