# @Program: File IO Methods Python
# @Author: Saloni Malhotra
# @Date: 25-07-2026

# 1st Program Reading the file
# ____________________________________________________________

flOpen = open("fileIO2.txt", "r")
i = 0
while True:
    i += 1
    line = flOpen.readline()
    if not line:
        break
    print(line)
    print(i)  # 1,2,3,4 (loop runs 4 times)


# 2nd Program Reading the file
# ____________________________________________________________________________

flOpenRead = open("fileIO3.txt", "r")
j = 0
while True:
    j += 1
    line = flOpenRead.read()
    if not line:
        break
    print(line)
    print(
        j
    )  # -> 1 (loop runs one time as it fetch all the content one time and print the data)

# 3rd Program
# _________________________________________________________________________________

fl = open("fileIO3.txt", "r")

while True:
    line = fl.readline()

    if not line:
        break

    m1 = line.split(",")[0]
    m2 = line.split(",")[1]
    m3 = line.split(",")[2]
    m4 = line.split(",")[3]

    print("m1 value is:", m1)
    print("m2 value is:", m2)
    print("m3 value is:", m3)
    print("m4 value is:", m4)
    print(line)

fl.close()


# 4th Program Write the Lines => writelines
# ____________________________________________________________

flwrite = open("fileIO2.txt", "w", encoding="utf-8")

employee_data = [
    "John,25,Software Engineer,New York\n",
    "Emma,30,Data Scientist,California\n",
    "Michael,28,Frontend Developer,Texas\n",
    "Sophia,27,Backend Developer,Florida\n",
    "William,31,DevOps Engineer,Washington\n",
    "Olivia,26,UI/UX Designer,Chicago\n",
    "James,29,Cloud Engineer,Boston\n",
    "Ava,24,QA Engineer,Seattle\n",
    "Benjamin,32,Product Manager,Austin\n",
    "Charlotte,28,AI Engineer,San Francisco\n",
]

flwrite.writelines(employee_data)
flwrite.close()


# 5th Program Write the Lines => write
# ____________________________________________________________

flwrite = open("fileIO3.txt", "w", encoding="utf-8")

books = [
    "B101,The Alchemist,Paulo Coelho,Fiction\n",
    "B102,Atomic Habits,James Clear,Self Help\n",
    "B103,Clean Code,Robert C. Martin,Programming\n",
    "B104,Python Crash Course,Eric Matthes,Programming\n",
    "B105,The Psychology of Money,Morgan Housel,Finance\n",
    "B106,Think and Grow Rich,Napoleon Hill,Motivation\n",
    "B107,Deep Work,Cal Newport,Productivity\n",
    "B108,The Hobbit,J.R.R. Tolkien,Fantasy\n",
    "B109,Harry Potter,J.K. Rowling,Fantasy\n",
    "B110,Rich Dad Poor Dad,Robert Kiyosaki,Finance\n",
]

for book in books:
    flwrite.write(book)

flwrite.close()
