# @Program: argparse in Python
# @Author: Saloni Malhotra
# @Date: 28-07-2026

import argparse
import shutil

# Example 1: Student Details ⭐
# ____________________________________________________________

parser = argparse.ArgumentParser(description="Student Details")


parser.add_argument("name", help="Student Name")
parser.add_argument("student_id", help="Student Id")
parser.add_argument("--age", type=int, default=18, help="Student Age")
parser.add_argument("--course", default="Python", help="Course Name")

args = parser.parse_args()

# Run through Command Line => python argparse-python.py "Saloni Malhotra" 1 --age 30 --course React. It will print the below records

print("Student Information")
print("----------------------------")
print("Name         :", args.name)
print("Student ID   :", args.student_id)
print("Age          :", args.age)
print("Course       :", args.course)


# Example 2: File Backup Script ⭐⭐ (Real World)
# ___________________________________________________________

parser = argparse.ArgumentParser(description="Backup a File")

parser.add_argument("source", help="Source File")
parser.add_argument("destination", help="Destination File")

args = parser.parse_args()

# python argparse-python.py D:\python\dummy-image.png D:
try:
    copied_file = shutil.copy(args.source, args.destination)
    print("Copied to:", copied_file)

    print("Backup Completed Successfully!")
    print("Source      :", args.source)
    print("Destination :", args.destination)
    print("Backup completed successfully.")

except Exception as e:
    print("Error:", e)
