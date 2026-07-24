# @Program: File IO Python
# @Author: Saloni Malhotra
# @Date: 24-07-2026


fileContent = """
File I/O -> in Python means File Input and Output. 
    1. Input -> Reading data from a file.
    2. Output -> Writing data to a file.
Instead of taking input from the keyboard (input()) or printing to the console (print()), 
you can save data in files and read it later.
"""


flAppendContent = """
a->  Appends adds the content everytime we append something.
w -> write overwrite the previous content.
"""


fileOpenContent = """
open automatically closes the file after performing the operation.
No need to manually call the close() method
"""

# 1st Program Reading the file
# _________________________________________________


def fileRead(fileName: str):
    flRead = open(fileName, "r")

    # Reading dir
    print(dir(flRead))

    # Size
    print(flRead.__sizeof__())

    # Read
    flContent = flRead.read()
    print(flContent)
    flRead.close()


# 2nd Program Writing the file
# ______________________________________________________________

flWrite = open("mynewFile.txt", "w", encoding="utf-8")
flWrite.write(fileContent)
flWrite.close()
fileRead("mynewFile.txt")


# 3rd Program Appending the data in the file
# ________________________________________________________________

flAppend = open("mynewFile.txt", "a", encoding="utf-8")
flAppend.write(flAppendContent)
flAppend.close()
fileRead("mynewFile.txt")

# 4th Program with statement
# _______________________________________________________________

with open("mynewFile.txt", "a", encoding="utf-8") as f:
    f.write(fileOpenContent)
    
fileRead("mynewFile.txt")

    
# Remove the file from the folder automatically after performing the actions
import os
os.remove("mynewFile.txt")