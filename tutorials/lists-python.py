# @Program: Lists in Python
# @Author: Saloni Malhotra
# @Date: 03-07-2026


# 1st Program of List        
# ---------------------------------------------------------------------

name = ["Saloni", "Anmol", "Jimmy", "Kartik"]

print(name[0])
print(name[1])
print(name[2])
print(name[3])

# -------------------------------------------------------------------------

for nm in name:
    print("User Names are below:")
    print(nm)
    
# -------------------------------------------------------------------------
if "Jimmy" in name:
    print("Yes, It Exist")
else:
    print("No, It doesn't Exist")
    

# -------------------------------------------------------------------------
if 67 in name:
    print("Yes, It Exist")
else:
    print("No, It doesn't Exist")

# -------------------------------------------------------------------------
lst = [i for i in range(15)]
print("The List Items are:", lst)
print(lst[:])
print(lst[1:6])
print(lst[:-8]) # 0 : len[range] - 8
print(lst[1:10:2])

# -------------------------------------------------------------------------
lstItems = [i*i for i in range(11) if i % 2 == 0]
print("The Event Number Items are:", lstItems)

