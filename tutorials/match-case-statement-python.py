# @Program: Match case Statement in Python
# @Author: Saloni Malhotra
# @Date: 30-06-2026


# 1st Program of match Case Statement
# ---------------------------------------------------------------------

userInput = int(input("Enter any number between 1 to 100: "))

match userInput:

    case 0:
        print("User Input is Zero")

    case 20 if userInput % 2 == 0:
        print("Condition is fully Satisfied")

    case _ if userInput < 0:
        print("Default Case: Number is not in Range between 1 to 100")

    case _:
        print("No Case")


# 2nd Program of match Case Statement
# ---------------------------------------------------------------------

userInputDay = input("Enter any day from Monday to Sunday: ")

match userInputDay.lower().strip():

    case "monday" | "tuesday" | "wednesday":
        print("Its", userInputDay.strip(), "& its coming in week first 3 Days.")

    case "thursday" | "friday" | "saturday":
        print("Its", userInputDay.strip())

    case "sunday":
        print("Yupiee Its", userInputDay.strip())

    case _:
        print("oops! Invalid Entry", userInputDay.strip())
