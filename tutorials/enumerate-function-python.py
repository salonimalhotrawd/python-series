# @Program: Enumerate Function in Python
# @Author: Saloni Malhotra
# @Date: 06-07-2026

marks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


# 1st Program without enumerate
# ______________________________________________________


index = 1
for mark in marks:
    print(f"Without Enumerate: {index}. {mark}")
    index += 1

print("\n")

# 2nd Program with enumerate
# ______________________________________________________

for index, mark in enumerate(marks):
    print(f"With Enumerate: {index + 1}. {mark}")
