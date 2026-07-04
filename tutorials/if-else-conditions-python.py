# @Program: If,Else & nested If Else Conditions in Python
# @Author: Saloni Malhotra
# @Date: 29-06-2026


num = int(input("Enter the number: "))


# 1st Program of If Else
# ---------------------------------------------------------------------

if num < 0:
    print("Number is Negative")
elif num == 0:
    print("Number is Zero")
else:
    print("Number is Positve")


"""
 Nested If Else Statement Example
"""
# 2nd Program of If Else
# -------------------------------------------------------------------------


if num < 0:
    print("Number is Negative")
elif num == 0:
    print("Number is Zero")
else:
    if num >= 1 and num <= 15:
        print("Number is in Between 10 to 15")
    else:
        print("Number is Greator than 15")
