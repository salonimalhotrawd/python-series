# @Program: Recursion in Python
# @Author: Saloni Malhotra
# @Date: 04-07-2026

# 1st Program in Recursion
# Factorial Program
# ---------------------------------------------------------------------------------


def factorial(num):
    """
    Calculate factorial of num using Recursion
    """
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)


userInput = int(input("Enter the user Input is: "))
print("User Input is: ", userInput, "\n")
result = factorial(userInput)
print("Factorial is:", result)


# Fibonacci Series
# -------------------------------------------------------------------------------------


def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


terms = int(input("Enter the number of terms: "))

for i in range(terms):
    print(fibonacci(i), end=" ")
