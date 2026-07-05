quizQuestions = [
    {
        "question": "What is the capital of India?",
        "options": ["Mumbai", "New Delhi", "Chennai", "Kolkata"],
        "answer": 2,
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Jupiter", "Mars", "Venus"],
        "answer": 3,
    },
    {
        "question": "Who is known as the Father of Computers?",
        "options": ["Charles Babbage", "Alan Turing", "Bill Gates", "Steve Jobs"],
        "answer": 1,
    },
    {
        "question": "Which programming language is primarily used with React?",
        "options": ["Python", "Java", "JavaScript", "C++"],
        "answer": 3,
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["func", "define", "function", "def"],
        "answer": 4,
    },
    {
        "question": "Which company developed React?",
        "options": ["Google", "Microsoft", "Meta (Facebook)", "Amazon"],
        "answer": 3,
    },
    {
        "question": "Which HTML tag is used to create a hyperlink?",
        "options": ["<a>", "<p>", "<img>", "<link>"],
        "answer": 1,
    },
    {
        "question": "Which CSS property is used to change the text color?",
        "options": ["font-color", "text-color", "color", "background-color"],
        "answer": 3,
    },
    {
        "question": "Which Python data type is immutable?",
        "options": ["List", "Dictionary", "Set", "Tuple"],
        "answer": 4,
    },
    {
        "question": "Which operator is used for exponentiation in Python?",
        "options": ["^", "**", "//", "%"],
        "answer": 2,
    },
    {
        "question": "What does API stand for?",
        "options": [
            "Application Programming Interface",
            "Advanced Programming Interface",
            "Application Process Integration",
            "Automated Programming Interface",
        ],
        "answer": 1,
    },
    {
        "question": "Which JavaScript method prints output to the browser console?",
        "options": ["print()", "console.log()", "echo()", "display()"],
        "answer": 2,
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["//", "#", "/* */", "--"],
        "answer": 2,
    },
    {
        "question": "Which data structure follows the FIFO principle?",
        "options": ["Stack", "Queue", "Tree", "Graph"],
        "answer": 2,
    },
    {
        "question": "Who created the Python programming language?",
        "options": [
            "Dennis Ritchie",
            "James Gosling",
            "Guido van Rossum",
            "Bjarne Stroustrup",
        ],
        "answer": 3,
    },
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
