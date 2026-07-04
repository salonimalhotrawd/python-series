# @Program: Lists Method in Python
# @Author: Saloni Malhotra
# @Date: 03-07-2026


# 1st Program of List Method
# Append Method in List
# ---------------------------------------------------------------------

lstKey = []
for i in range(15):
    lstKey.append(i)

print("The List are:", lstKey)

# Reverse Method in Lists
lstKey.reverse()
print("Reverse List are:", lstKey)

# sort Method in Lists
inputNumber = [12, 45, 67, 89, 45, 21, 23, 34, 12, 0, 100]
inputNumber.sort()
print("Sorted Lists are: ", inputNumber)

# Index Method in Lists
print(
    "The 89 index is in placed: ", inputNumber.index(89)
)  # if the value not exists then error

# Count Method in Lists
print("The Count method are: ", inputNumber.count(45))

# Copy Method in Lists
m = inputNumber.copy()
m[0] = 200
print("Copy List are: ", m)

# Insert Method in Lists
m.insert(2, 10)
print("New insert List are:", m)

# Extend Method in Lists
lstKey.extend(m)
print("Extend Lists are: ", lstKey)

# concatenation of two Lists
n = [10, 90, 34, 5, 67, 8] + m
print("New Concatenated Lists are:", n)
