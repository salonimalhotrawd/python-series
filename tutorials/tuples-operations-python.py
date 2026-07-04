# @Program: Tuples Operations in Python
# @Author: Saloni Malhotra
# @Date: 04-07-2026

# Tuple

tup = ("Red", "Violet", "Indigo", "Brown", "Green", "Yellow", "Orange", "Red")

# Count
print("The Coubt Res is: ", tup.count("Red"), "\n")

# Length
print("The Length of the Tup is: ", len(tup), "\n")

# Indexes
print("The Indexes of the tup is: ", tup.index("Violet"), "\n")

print("The Indexes of the tup is: ", tup.index("Red", 2, 8), "\n")  # 7

print("The Indexes of the tup is: ", tup.index("Red", 0, 8), "\n")  # 0


# Tup Can't be change so we create the copy and append its value
temp = list(tup)
temp.append("White")  # Add
temp.remove("Red")  # pop
temp[3] = "Black"
tup = tuple(temp)
print("The Copy of the tuple is: ", tup, "\n")


# concatenation of two tuples and create new one

countries1 = ("India", "Pakistan", "UK", "USA", "Rome")
countries2 = ("Europe", "Azerbizaan", "Egypt", "Switzerland")
countries3 = countries1 + countries2
print("The New Concatenated Countries are: ", countries3)
