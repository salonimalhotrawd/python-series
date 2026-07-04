# @Program: Dictionary Methods in Python
# @Author: Saloni Malhotra
# @Date: 04-07-2026

dict1 = {"name": "Saloni Malhotra", "age": 31, "status": "Married"}
dict2 = {"name": "Anmol Dogra", "age": 32, "status": "Married"}
dict3 = {123: "Saloni Malhotra", 456: "Anmol Dogra"}

# Update Method of Dictionary
dict1.update(dict2)

# => If both the keys are same then it override the value of dict1
# dict1 => {"name": "Anmol Dogra", "age": 32, "status": "Married"} & dict2 => {"name": "Anmol Dogra", "age": 32, "status": "Married"}
# __________________________________________________________________________________________________________________________________________
print("Update dict1 values are: ", dict1, "\n", dict2, "\n")


# Update dict1 values are:  {'name': 'Anmol Dogra', 'age': 32, 'status': 'Married', 123: 'Saloni Malhotra', 456: 'Anmol Dogra'}
# {123: 'Saloni Malhotra', 456: 'Anmol Dogra'}
# __________________________________________________________________________________________________________________________________________
dict1.update(dict3)
print("Update dict1 values are: ", dict1, "\n", dict3, "\n")


# del dict3 Dictionary (dict3 is already deleted so nothing prints and throws an error)
# Output => NameError: name 'dict3' is not defined. Did you mean: 'dict1'?
# __________________________________________________________________________________________________________________________________________
del dict3
print("dict3 are: ", dict3, "\n")

# clear dict3 Dictionary
# Output => dict3 clear are:  {}
# __________________________________________________________________________________________________________________________________________
dict3.clear()
print("dict3 clear are: ", dict3, "\n")

# pop dict3 Dictionary
# Output => {456: 'Anmol Dogra'}
# if key doesn't exists then it will throw an error:  KeyError: '1ssssssss23'
# __________________________________________________________________________________________________________________________________________
dict3.pop("1ssssssss23")
print("dict3 123 pop Items are: ", dict3, "\n")

# popItem dict3 Dictionary
# Output => {123: 'Saloni Malhotra'}
# __________________________________________________________________________________________________________________________________________
dict3.popitem()
print("dict3 pop Items are removed Item from the past : ", dict3, "\n")
