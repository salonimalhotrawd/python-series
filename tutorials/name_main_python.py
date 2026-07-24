# @Program: __name__ == "__main__" in Python
# @Author: Saloni Malhotra
# @Date: 04-07-2026

''' 
    The Problem with Imports: By default, when you import a module in Python, any code (like function calls or print statements) written at the top level of that module is executed immediately. This can lead to unintended side effects when you only wanted to access a specific function.
    
    Solution (if __name__ == "__main__":): This condition checks whether the script is being run directly by the user or if it is being imported as a module in another file
    
    If the script is executed directly, __name__ is set to "__main__", and the code inside the block runs
    
    If the script is imported into another file, __name__ is set to the name of the module (e.g., "name_main_python"), and the code inside the if block is skipped
'''

# 1st Program in Python
#_______________________________________________________________________


def welcome():
    print("Hi, Welcome! My Name is Saloni Malhotra")
    
print(__name__)

if __name__ == "__main__":
    welcome()
