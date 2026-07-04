# @Program: TypeCasting in Python
# Two types : Explicit & Implicit TypeCasting
# @Author: Saloni Malhotra
# @Date: 23-06-2026

num1 = "10"
num2 = "20"

print(num1 + num2)  # 1220 (as type is string)

print(int(num1) + int(num2))  # 30


# In Implicit typecasting lower order data type is automatically converted into higher order data type by python interpreter
# so that no data is lost

num3 = 10.5
num4 = 5


print(
    "Type of num3 is:", type(num3), "& Type of num4 is:", type(num4)
)  # num3 => float, num4 => int
print(num3 + num4, type(num3 + num4))  # 15.5, type is float
