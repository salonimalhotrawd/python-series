# @Program: For Loop in Python
# @Author: Saloni Malhotra
# @Date: 30-06-2026


# 1st Program of for loop
# ---------------------------------------------------------------------

name = input("Enter the name: ")

for i in name:
    print("Keys in String:", i)


# 2nd Program of for loop
# ---------------------------------------------------------------------

users = ["anmol", "saloni", "jimmy"]

for user in users:
    print("List of users are: ", user)
    for k in user:
        print("Each alphabet of user is: ", k)

# 3rd Program of for loop
# ---------------------------------------------------------------------

for z in range(9):
    print(
        "Range are: ", z
    )  # it starts from 0 to 8, i mean n-1 so if range is 9 then it will execute 9-1 which is 8


# 4th Program of for loop
# ---------------------------------------------------------------------

for rng in range(1, 10):
    print("Print the numbers from 1 to 9: ", rng)

# 5th Program of for loop
# ---------------------------------------------------------------------

for values in range(1, 15, 2):
    print("It will skipped 2 values from iteration i mean it will do i+2: ", values)
