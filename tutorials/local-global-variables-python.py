# @Program: Local & Global Variables in Python
# @Author: Saloni Malhotra
# @Date: 24-07-2026


# 1st Program in local & Global Variables
# ___________________________________________________________

x = 10
print("Global Variable:", x) # 10

def my_function():
    global x
    x = 5
    y = 1
    print("Local Variable:", y) # 1

my_function()
print("Global Variable:", x) # 5
print("y Variable is:", y) # NameError: name 'y' is not defined