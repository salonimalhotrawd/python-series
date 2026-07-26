# @Program: Map, Filter, Reduce in Python
# @Author: Saloni Malhotra
# @Date: 26-07-2026


user_numbers = [1, 2, 3, 4, 5]


# 1st Program Reading the file => Map Function
# _______________________________________________________________________
 
new_numbers = map(lambda x: x * x * x, user_numbers)

print(new_numbers) # <map object at 0x000001565574A9E0>

print(list(new_numbers)) # [1, 8, 27, 64, 125]


# 2nd Program Reading the file => Filter Function
# _________________________________________________________________________
 
new_numbers_filter = list(filter(lambda x: x > 2, user_numbers))

print(new_numbers_filter) # [3,4,5]

# 3rd Program Reading the file => Reduce Function
# ________________________________________________________________________

from functools import reduce

new_numbers_reduce = reduce(lambda x,y: x+y, user_numbers)

print(new_numbers_reduce)