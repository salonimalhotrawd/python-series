# @Program: Airthmetic, Comparison & Logical Operators in Python
# @Author: Saloni Malhotra
# @Date: 23-06-2026


# 1st Program of Airthmetic Operators
# ---------------------------------------------------------------------

num1 = 10
num2 = 10

print("Addition of num1 & num2:", num1 + num2)
print("Subtraction of num1 & num2:", num1 - num2)
print("Multiplication of num1 & num2:", num1 * num2)
print("Division of num1 & num2:", num1 / num2)
print("Floor Division of num1 & num2:", num1 // num2)
print("Modulus of num1 & num2:", num1 % num2)
print("Exponential of num1 & num2:", num1**num2)

# 1st Program of Comparison Operators
# -------------------------------------------------------------------------
print("Is num1 is equal to num2", num1 == num2)
print("Is num1 is not equal to num2", num1 != num2)
print("Is num1 is greator than num2", num1 > num2)
print("Is num1 is less than equal to num2", num1 <= num2)

# 1st Program of Logical Operators
# -------------------------------------------------------------------------
userAge = 10
has_licence = False

print("Is User is Eligible for Driving?", userAge >= 18 and has_licence)
print("Is User is Eligible for Driving?", userAge >= 18 or has_licence)
print("Is User is Adult ?", not userAge < 18)
