# @Program: Decorators in Python
# @Author: Saloni Malhotra
# @Date: 26-07-2026


"""
A decorator is a function that adds extra functionality to another function without changing its original code. It "wraps" the original function and executes additional code before or after it. Decorators are commonly used for logging, authentication, timing, validation, and access control.

"""

# 1st Program -> Normal function pass to another function
# _________________________________________________________


def sayHiMessage():
    print("Hello World")


def greet(fx):
    def mfx():
        print(f"\n*************** Good Morning ****************")
        fx()
        print("\n**************** Good Evening ***************")

    return mfx


greet(sayHiMessage)()

# 2nd Program in Decorators
# _______________________________________________________________


@greet
def welcome():
    print("\nWelcome to Python!")


welcome()

# 3rd Program in Decorators
# ____________________________________________________________________

"""
    *args (Non-keyword/Positional Arguments)
        => It collects multiple positional arguments into a tuple.
        
        Example => 
            def displayNumbers(*args):
            print(args) => (10,20,30,40)

            displayNumbers(10, 20, 30, 40)
"""


"""
    **kwargs (Keyword Arguments)
         => collects multiple keyword arguments into a dictionary.
         
        Example => 
            def displayEmployee(**kwargs):
                print(kwargs)

            displayEmployee(
                id=1,
                name="Saloni",
                designation="Associate Product Lead"
            )
            
        Output => 
            {'id': 1, 'name': 'Saloni', 'designation': 'Associate Product Lead'}
"""


def decorator_function(fx):

    def wrapper_function(*args, **kwargs):

        print("Before the function executes")

        fx(*args, **kwargs)

        print("After the function executes")

    return wrapper_function


@decorator_function
def additionOfTwoNumbers(a, b):
    print(a + b)


additionOfTwoNumbers(10, 100)
