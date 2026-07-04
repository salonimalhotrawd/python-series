# @Program: Exception Handling & Finally Keyword in Python
# @Author: Saloni Malhotra
# @Date: 04-07-2026

userInput = input("Enter any userInput: ")
print("userInput is: ", userInput)


# 1st Way
# -------------------------------------------------------------------------
try:
    for i in range(1, 11):
        print(f"Print {int(userInput)} X {i} =  {int(userInput)} * {i}")
except Exception as e:
    print(e)


# 2nd Way
# ----------------------------------------------------------------------------
try:
    for i in range(1, 11):
        print(f"Print {int(userInput)} X {i} =  {int(userInput)} * {i}")
except:
    print("Invalid Input! please input correct integer Value")


# 3rd Way
# -----------------------------------------------------------------------------
def sumOfTwoNumbers(a, b):
    try:
        if a > 10:
            print(f"Values of a & b is: {a},{b} ")
            return a + b
    except:
        print("Invalid Output")

    finally:
        print("This Block is always Executed")


sumOfTwoNumbers(12, 450)

# 4th Way
# Custom Errors Handling
# ----------------------------------------------------------------------------------


def handlingCustomErrors(num):
    if num < 20:
        raise ValueError("Value should be greator than 10")
    else:
        print(f"User Input is: {num}")


handlingCustomErrors(10)
