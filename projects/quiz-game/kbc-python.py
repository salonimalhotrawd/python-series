# @Program: KBC Projects in Python
# @Author: Saloni Malhotra
# @Date: 05-06-2026

from gameData import kbcQuestions, levels

takeHomeMoney = 0


def format_money(amount):
    return f"₹{amount:,}"


for i in range(0, len(kbcQuestions)):
    question = kbcQuestions[i]
    level = levels[i]
    print(f"\nQuestion for Rs. {level}")
    print(question[0])

    print(f"1. {question[1]}")
    print(f"2. {question[2]}")
    print(f"3. {question[3]}")
    print(f"4. {question[4]}")

    reply = input("Enter your answer (1-4) or type 'yes' to quit: ")
    if reply.lower() == "yes":
        print(f"Opps! You have quit the game")
        if i > 0:
            takeHomeMoney = levels[i - 1]
    elif int(reply) == question[6]:
        print(f"Correct Answer you have won Rs: {format_money(level)}")
        if i == 4:
            takeHomeMoney = 10000
        if i == 9:
            takeHomeMoney = 320000
        if i == 14:
            takeHomeMoney = 10000000
    else:
        print("Wrong Answer")
        break
    print("\n")

print(f"Your take home money is: Rs. {format_money(takeHomeMoney)}")
