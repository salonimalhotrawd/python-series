# @Program: Sets in Python
# @Author: Saloni Malhotra
# @Date: 04-07-2026

# Sets are unordered collection of data items. They store multiple items in a single variable.
# Set items are seperated with commas and enclosed within curly brackets {}
# Sets are unchangeable,means we cannot change the value once created
# Sets do not contains multiple items
# -----------------------------------------------------------------------------------------------------

# 1st Program of Sets
# ----------------------------------------------------------------------

userSet = {"12", "Saloni", "78", "90", "12", "Saloni", "Zaid", "12", "23"}

print("User Set are: ", userSet)
print("User Set Type are: ", type(userSet))

# 2nd Program of Sets
# If we create empty set like this => {} then its not set its dict
# -----------------------------------------------------------------------

aa = {}
print("Sets are: ", type(aa))  # => <class 'dict'>

# 3rd Program of Sets
# if we create empty set then by using set we can easily do it
# -------------------------------------------------------------------------

bb = set()
print(type(bb))
