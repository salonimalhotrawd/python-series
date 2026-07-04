# @Program: Sets Method in Python
# @Author: Saloni Malhotra
# @Date: 04-07-2026


s1 = {1, 2, 3, 4, 5}
s2 = {3, 5, 6, 7, 8}

# Union Method in Sets
# ---------------------------------------------------------------------------------------------
print("Union of two sets s1 & s2 are", s1.union(s2))  # {1,2,3,4,5,6,7,8}

# Update Method in Sets
# ----------------------------------------------------------------------------------------------

s1.update(s2)
print("updates sets are: ", s1, s2)  # s1 => {1,2,3,4,5,6,7,8} , s2 => {3,5,6,7,8}

# Intersection Method in Sets
# ----------------------------------------------------------------------------------------------
print(
    "Intersection of two sets s1 & s2 are", s1.intersection(s2)
)  # {3,5}  => Common in Both

# Intersection Update Method in Sets
# ----------------------------------------------------------------------------------------------
s1.intersection_update(s2)
print("Intersection Updates Sets are: ", s1, s2)  # s1 => {3,5} , s2 => {3,5,6,7,8}

# Symmetric Difference Method in Sets
# -----------------------------------------------------------------------------------------------------------------------
print(
    "Symmetric Difference of two sets s1 & s2 are", s1.symmetric_difference(s2)
)  # {1,2,4,6,7,8} => Not Common in Both

# Symmetric Difference Update Method in Sets
# ----------------------------------------------------------------------------------------------------------------------------
s1.symmetric_difference_update(s2)
print(
    "Intersection Updates Sets are: ", s1, s2
)  # s1 => {1,2,4,6,7,8} , s2 => {3,5,6,7,8}

# Difference Method in Sets
# that are only present in the original sets not in the both sets
# ----------------------------------------------------------------------------
print("Difference of two sets s1 & s2 are", s1.difference(s2))  # {1,2,4}

# Difference Update Method in Sets
# ----------------------------------------------------------------------------------------------------------------------------
s1.difference_update(s2)
print("Difference Updates Sets are: ", s1, s2)  # s1 => {1,2,4} , s2 => {3,5,6,7,8}

# isdisjoint() Method in Sets
# -----------------------------------------------------------------------------------------------------------------------
print("isdisjoint of two sets s1 & s2 are", s1.isdisjoint(s2))  # False

# issuperset Method in Sets
# ----------------------------------------------------------------------------
print("issuperset of two sets s1 & s2 are", s1.issuperset(s2))

# issubset Method in Sets
# ----------------------------------------------------------------------------
print("issubset of two sets s1 & s2 are", s1.issubset(s2))

# Add Method in Sets
# ----------------------------------------------------------------------------

s1.add(90)
print("Add in 90 Sets are => ", s1)  # 90

# Remove Method in Sets
# It will throw an error if the value doesn't exist
# ----------------------------------------------------------------------------

s1.remove(3)
print("Remove 3 from sets are => ", s1)  # {1,2,4,5}

s1.remove(90)
print(
    "Remove 90 from sets are => ", s1
)  # File "D:\python-series\tutorials\sets-method-python.py", line 70, in <module>, s1.remove(90), KeyError: 90

# Discard Method in Sets
# ----------------------------------------------------------------------------
s1.discard(90)
print(
    "Discard 90 from sets are => ", s1
)  # doesn't throw an error => Same Set => Not Showing an error

# Pop Method in Sets
# ------------------------------------------------------------------------------
s1.pop()
print(
    "Pop from the sets are and it is unordered you can't detect which one is pop from the set: ",
    s1,
)

# Del Method in Sets
# -----------------------------------------------------------------------------
del s1
print(
    "s1 sets is deleted:", s1
)  # => it throws an error as s1 is deleted => NameError: name 's1' is not defined. Did you mean: 's2'?

# clear Method in Sets
# -----------------------------------------------------------------------------
s1.clear()
print("s1 clear sets are: ", s1)  # => set()
