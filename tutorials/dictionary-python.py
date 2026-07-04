# @Program: Dictionary in Python
# @Author: Saloni Malhotra
# @Date: 04-07-2026


user = {"name": "Saloni Malhotra", "age": 31, "status": "Married"}

print("user Dictionary is: ", user)
print("Type of user Dictionary is: ", type(user))

# Accessing Keys from Dictionary
# ------------------------------------------------------------------------
print("user Dictionary Keys are: ", user.keys())

# Accessing values from Dictionary
# ------------------------------------------------------------------------
print("user Dictionary Values are: ", user.values())

# Accessing items from Dictionary
# ------------------------------------------------------------------------
print("user Dictionary Items are: ", user.items())

# Accessing key from user.keys()
# -------------------------------------------------------------------------
for key in user.keys():
    print(f"User Key is '{key}' and its value is: {user[key]}")

# Accessing key,value from user.items()
# -------------------------------------------------------------------------
for key, value in user.items():
    print(f"User Key is '{key}' and its value is: {value}")
