# @Program: os Module in Python
# @Author: Saloni Malhotra
# @Date: 24-07-2026

import os
import shutil

#___________________________________________________

print(dir(os))

# Make Directory
if(not os.path.exists("os_practice")):
    os.mkdir("os_practice")
    
# Make Directory
for i in range(1,100):
    os.mkdir(f"os_practice/Tutorial {i}")
    
# Rename Directory
for i in range(1,100):
    os.rename(f"os_practice/Day{i}", f"os_practice/Tutorial {i}")

# Remove Directory
for i in range(1,100):
    os.removedirs(f"os_practice/Tutorial {i}")
    
# shutil.rmtree("os_practice")
    
    
