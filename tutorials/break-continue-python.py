# @Program: Break Cntinue Statement in python in Python
# @Author: Saloni Malhotra
# @Date: 30-06-2026


# 1st program of continue statement in Python
# --------------------------------------------------
num = int(input("Enter the number: "))

for i in range(1, num):
    if i % 2 == 0:
        print("Skip this iteration ", i)
        continue
    print("I am Executing", i)

print("I am out of loop")


# 1st program of break statement in Python
# --------------------------------------------------

for i in range(1, 20):
    if i == 15:
        break
    print("5 *", i, "=", 5 * i)

print("I am out of loop")
