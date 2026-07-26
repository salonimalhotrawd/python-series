# @Program: dir, dict and help in Python
# @Author: Saloni Malhotra
# @Date: 27-07-2026


# 1st program => dir
# ________________________________________________
x = [1,2,3,4]
print("\n")
print("=" * 100)
print(dir(x))


# 2nd Program -> dict
#__________________________________________________

class Employee:

    def __init__(self, name, salary, password):

        self.name = name  # Public
        self._salary = salary  # Protected
        self.__password = password  # Private


emp = Employee("Saloni", 5000000, "Saloni@1234")
print("\n")
print("=" * 100)
print(emp.__dict__)

# 3rd Program
#_______________________________________________________

print(help(str),"\n")
print(help(tuple),"\n")
print(help(list),"\n")
print(help(dict),"\n")
print(help(Employee),"\n")