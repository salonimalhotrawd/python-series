# @Program: Functions in Python
# @Author: Saloni Malhotra
# @Date: 30-06-2026


# 1st Program of function
# ---------------------------------------------------------------------


def sumOfTwoNumbers(a, b):
    sum = a + b
    print("Sum of Two numbers", a, "&", b, "is =", sum)


firstNumber = int(input("Enter the first Number: "))
secondNumber = int(input("Enter the Second Number: "))

sumOfTwoNumbers(firstNumber, secondNumber)

# 2nd Program of function
# eval Method
# ------------------------------------------------------------------------


def mathematicOperationsOfNumbers(a, b, operationToPerformed):
    result = f"{a} {operationToPerformed} {b}"
    print(eval(result))


mathematicOperationsOfNumbers(10, 90, "*")

# 3rd Program of function
# return Method
# ------------------------------------------------------------------------


def printfullName(fName, lName):
    return fName + " " + lName


fullName = printfullName("Saloni", "Malhotra")
print("My FullName is:", fullName)

# 4th Program of function
# Functions Arguments
# ------------------------------------------------------------------------


def printCurrentDayandTime(day, time):
    print("Current Day is", day, "& Time is", time)


printCurrentDayandTime("Tuesday", "6:15 PM")


# 5th Program of function
# Functions Default Arguments
# ------------------------------------------------------------------------


def printMyData(fName, lName, city="Amritsar"):
    print("My fullName is", fName + " " + lName, "& City is", city)


printMyData("Saloni", "Malhotra")
printMyData("Anmol", "Dogra", "Hamirpur")
printMyData(
    lName="Dogra", city="Ludhiana", fName="Jimmy"
)  # order not matter if we add value as key name same as function Argument Name
