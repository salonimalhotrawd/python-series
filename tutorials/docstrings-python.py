# @Program: docstrings in Python
# @Author: Saloni Malhotra
# @Date: 04-07-2026

# 1st Program on Doc String
# It is used for documentation purpose and its written at the firstplace in function
# we case access docstrings with help or __doc__
# ------------------------------------------------------------------------------------


def userFxn():
    """
    @author: Saloni Malhotra
    This function takes two values and return the sum of a & b
    """
    a = int(input("Enter first Number -> "))
    b = int(input("Enter second Number -> "))

    result = a + b
    print(f"The output of a & b is: ", {result})


userFxn()
print("Given Function DocString are: ", userFxn.__doc__)
print("Given Function help Value are: ", help(userFxn))


# 2nd Program on docString
# ------------------------------------------------------------------------------------


def currentDayandMonth():
    month = "July"

    """
        if we add this after some condition or on the second place then doc value is none 
        It is always at the first place
    """

    day = "Saturday"

    print("The output of Current Day and Month is: ", day, month)


currentDayandMonth()
print("Given Function DocString are: ", currentDayandMonth.__doc__)
print("Given Function help Value are: ", help(currentDayandMonth))
