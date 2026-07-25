# @Program: File IO Methods Python
# @Author: Saloni Malhotra
# @Date: 25-07-2026

# 1st Program Seek Method
# ____________________________________________________________

seek_content = 300

with open("fileIO2.txt", "r") as f:

    f.seek(seek_content)
    print("file Tell Before read: ", f.tell(), "\n")
    data = f.read(54)
    print("file Tell After read: ", f.tell(), "\n")
    print(
        "---------------------------- After Seeking data is -----------------------: \n",
        data,
    )

# 2nd Program
# _________________________________________________________________________________

content = (
    "Python is a programming language.It is simple.It is powerful.It is used for AI."
)

with open("demoIO.txt", "w+") as f:
    f.write(content)
    print("After write:", f.tell())
    f.seek(6)
    print("After seek:", f.tell())
    f.truncate(10)
    f.seek(0)
    data = f.read()
    print(repr(data))
    print(data)

# 3rd Program
# _________________________________________________________________________________

with open("demoIO.txt", "w+") as f:
    f.write(content)
    f.seek(6)
    print("Before truncate:", f.tell())
    f.truncate()
    print("After truncate:", f.tell())
    print("Read:", repr(f.read()))
    f.seek(0)
    print("After seek(0):", repr(f.read()))
