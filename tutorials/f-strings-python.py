# @Program: f-strings in Python
# @Author: Saloni Malhotra
# @Date: 04-07-2026


# 1st way of appending the literals in string
# -----------------------------------------------------------

userString = "Hey my fullName is {} and I am living in {}"

fullName = "Saloni Malhotra"
state = "Amritsar"

print("The full UserString is: ", userString.format(fullName, state), "\n")


# 2nd way of appending the literals in string
# -------------------------------------------------------------------

employeeData = "Hey I am {1} and I am working in {0}"
fullNm = "Saloni Malhotra"
companyName = "Microsoft"

print("****************************************************************************")
print("The full Employee Info is: ", employeeData.format(companyName, fullNm), "\n")

# 3rd Way of appending the Literals in string
# --------------------------------------------------------------------------------

keyString = f"Hey my fullName is {fullName} and state is {state}"
print("The KeyString are: ", keyString)
