# @Program: Lambda Function Python
# @Author: Saloni Malhotra
# @Date: 25-07-2026


# 1st Program
# __________________________________________________


def additionofTwoSum(a, b):
    return a + b


sum = lambda a, b: a + b
double = lambda x: x * 2
cube = lambda y: y * y * y
avg = lambda x, y, z: (x + y + z) / 3

print(additionofTwoSum(10, 20))
print(sum(10, 20))
print(double(10))
print(cube(30))
print(avg(30, 50, 80))
