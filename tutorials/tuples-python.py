# @Program: Tuples in Python
# @Author: Saloni Malhotra
# @Date: 04-07-2026


# diff between tuple and list is we can change the list but we can't change the tuple like constants

# Tuple Practice
# ---------------------------------------------------------------------

tup = ("Red", "Green", "Pink", "Yellow", "Brown", "Violet")

print("Tuple Values are:", tup, "\n")

# Get Type
print("Type of Tuple is:", type(tup), "\n")

# Accessing Tuple through Indexes
print("Index 4 Tuple Value is:", tup[4], "\n")

# Length of the Tuple
print("Length of the tuple is: ", len(tup), "\n")

# Slicing happens in tuple but we can create it copy of new tuple
tup2 = tup[1:5]
print("New Tuple is: ", tup2, "\n")

# if condition in tuple
if "Pink" in tup:
    print("Yes Pink is exist in the Tuple", "\n")
else:
    print("No It does not exist in the tuple", "\n")

# -ve Indexes Tuple
print(tup[:], "\n")  # its 0:len(tup)

print(tup[:-3])  # tup[0: len(tup) - 3] => tup[0:3]
