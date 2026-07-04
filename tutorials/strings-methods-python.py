# @Program: Strings Method in Python
# @Author: Saloni Malhotra
# @Date: 23-06-2026


# Strings are immmutable in Python
name = "saloni malhotra"

# upper():
print(name.upper())  # SALONI MALHOTRA

# lower():
print(name.lower())  # saloni malhotra

# capitialize
print(name.capitalize())  # Saloni malhotra

# title Case
print(name.title())  # Saloni Malhotra


# Strip => It removes any white spaces before and after the string
str = "   Silver Spoon   "
print(str.strip())  # Silver Spoon


# rStrip => removes any trailing character after the string
str2 = "!!!! Hello!!! **** !!!!!"
print(str2.rstrip("!"))  # !!!! Hello!!! ****


# replace
print(str.replace(" ", "*"))  # ***Silver*Spoon***
print(str2.replace("Hello", "hahahhaha"))  # !!!! hahahhaha!!! **** !!!!!


# Split
print(name.split(" "))

# join
print(name.join(["Hi", "there"]))

# Center
print(name.center(50))

# Count
print(name.count("a"))

# startsWith()
print(name.startswith("s"))

# endsWith
print(name.endswith("a"))

# find
print(name.find("a"))

# index
print(name.index("i"))

# isalnum => returns true if only A-z,a-z,0-9 are present & if characters or any pucntuations are present than false
str = "welcometoconsole12"
print(str.isalnum())

# isalpha() => returns true if only A-z,a-z are present & if any others characters, numbers(0-9) or any pucntuations are present than false
print(str.isalpha())
