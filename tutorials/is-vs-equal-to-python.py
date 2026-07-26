# @Program: is vs == in Python
# @Author: Saloni Malhotra
# @Date: 26-07-2026

# 1st Program
# _______________________________________________________________________

a = 4
b = "4"

print(a is b)  # False => is checks the exact location of object in memory
print(a == b)  # False => == checks value is same


# 2nd Program
# _______________________________________________________________________

c = 3
d = 3

print(
    c is d
)  # True, In python it knows constant wont change so its points to the same memory address
print(c == d)  # True
