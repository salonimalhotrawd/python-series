# @Program: KBC Projects in Python
# @Author: Saloni Malhotra
# @Date: 05-7-2027

# @description:
#     Create a program capable of displaying questions to the user like KBC
#     Use List data type to store the questions and their correct answers
#     Display the final amount the person is taking home after playing the game

kbcQuestions = [
    [
        "What is the capital of India?",
        "Mumbai",
        "New Delhi",
        "Chennai",
        "Kolkata",
        "None",
        2,
    ],
    [
        "Which planet is known as the Red Planet?",
        "Earth",
        "Jupiter",
        "Mars",
        "Venus",
        "None",
        3,
    ],
    [
        "Who is known as the Father of Computers?",
        "Charles Babbage",
        "Alan Turing",
        "Bill Gates",
        "Steve Jobs",
        "None",
        1,
    ],
    [
        "Which programming language is primarily used for Android development?",
        "Swift",
        "Kotlin",
        "Python",
        "Ruby",
        "None",
        2,
    ],
    [
        "Which data type is immutable in Python?",
        "List",
        "Dictionary",
        "Set",
        "Tuple",
        "None",
        4,
    ],
    [
        "Which company developed the React library?",
        "Google",
        "Microsoft",
        "Facebook (Meta)",
        "Amazon",
        "None",
        3,
    ],
    [
        "Which keyword is used to define a function in Python?",
        "function",
        "func",
        "define",
        "def",
        "None",
        4,
    ],
    [
        "Which HTML tag is used to create a hyperlink?",
        "<img>",
        "<a>",
        "<p>",
        "<link>",
        "None",
        2,
    ],
    [
        "Which CSS property changes the text color?",
        "background-color",
        "font-size",
        "color",
        "text-align",
        "None",
        3,
    ],
    [
        "Which JavaScript method is used to print something in the browser console?",
        "print()",
        "console.log()",
        "echo()",
        "display()",
        "None",
        2,
    ],
    [
        "Which symbol is used for comments in Python?",
        "//",
        "/* */",
        "#",
        "--",
        "None",
        3,
    ],
    [
        "Which operator is used for exponentiation in Python?",
        "^",
        "**",
        "*",
        "//",
        "None",
        2,
    ],
    [
        "What does API stand for?",
        "Application Programming Interface",
        "Advanced Program Integration",
        "Application Process Integration",
        "Advanced Programming Internet",
        "None",
        1,
    ],
    [
        "Which company created the Python programming language?",
        "Google",
        "Microsoft",
        "Python Software Foundation",
        "Guido van Rossum",
        "None",
        4,
    ],
    [
        "Which data structure follows the FIFO principle?",
        "Stack",
        "Queue",
        "Tree",
        "Graph",
        "None",
        2,
    ],
]

levels = [
    1000,
    2000,
    3000,
    5000,
    10000,
    20000,
    40000,
    80000,
    16000,
    32000,
    640000,
    1250000,
    2500000,
    5000000,
    10000000,
]
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
    print(i)
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
