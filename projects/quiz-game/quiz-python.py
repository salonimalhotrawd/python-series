# @Program: KBC Projects in Python
# @Author: Saloni Malhotra
# @Date: 05-07-2026

from gameData import quizQuestions, levels

takeHomeMoney = 0


def format_money(amount):
    return f"₹{amount:,}"


for i in range(0, len(quizQuestions)):

    # Get Quiz Questions
    quiz = quizQuestions[i]

    # Get Levels
    level = levels[i]

    # Get Questions
    ques = quiz["question"]

    # Get Options
    options = quiz["options"]

    # Get Answer
    ans = quiz["answer"]

    # Labels for Displaying Index
    labels = ["a", "b", "c", "d"]

    print(f"\nQuestion for Rs. {level}")
    print(ques)
    for index, option in enumerate(options):
        print(f"{labels[index]}. {option} ")

    reply = input("Enter your answer (1-4) or type 'yes' to quit ")

    if reply == "yes":
        print("Oops! You have quit the Game")
        if i > 0:
            takeHomeMoney = levels[i - 1]
        break
    elif int(reply) == ans:
        print("Yupp!, Your answer is Correct")

        # Levels Calculation for takeHomeMoney
        if i == 4:
            takeHomeMoney = 10000
        if i == 9:
            takeHomeMoney = 32000
        if i == 14:
            takeHomeMoney = 10000000
    else:
        print("Wrong Answer")
        break
    print("\n")

print(f"Your take home money is: Rs. {format_money(takeHomeMoney)}")
