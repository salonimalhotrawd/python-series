# @Program: Strings Slicing & Operations in Python
# @Author: Saloni Malhotra
# @Date: 23-06-2026


name = "Saloni Malhotra"

# Finding Length of the String
print(len(name))

# Slicing in String

# Output is Saloni and left side index is included in slicing and right side is excluding in String Slicing
print(name[0:6])

# If before : left side value is missing then python automatically detect it as 0 index
print(name[:6])

# If only colon is present then whole length is considered by python so, output is Saloni Malhotra
print(name[:])

# If Negative Index is present then python will subtract the value from its total length
# print(name[1:-3]) => print(name[1: len(name) - 3])  => print(name[1:12])

print(name[1:-3])

# print(name[1:-3])  == print(name[1: len(name) - 3]) both are same
print(name[1 : len(name) - 3])

# Nothing happens => no output as 1 to -15 no value is exist
print(name[1 : len(name) - 30])
