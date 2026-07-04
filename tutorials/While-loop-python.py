# @Program: While Loop in Python
# @Author: Saloni Malhotra
# @Date: 30-06-2026


# 1st Program of While loop
# ---------------------------------------------------------------------

num = 1

while num <= 3:
    print(num)
    num = num + 1


# 2nd Program of While with Else loop
# ---------------------------------------------------------------------

userInput = int(input("Please Enter the number between 1 to 100: "))

while userInput <= 100:
    print(userInput)
    userInput = userInput + 1
else:
    print("I am out of range: ", userInput)
