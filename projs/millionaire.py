# Who Wants to Be a Millionaire Quiz

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. London", "B. Berlin", "C. Paris", "D. Madrid"],
        "correct": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
        "correct": "B"
    },
    {
        "question": "What is 2 + 2?",
        "options": ["A. 3", "B. 4", "C. 5", "D. 6"],
        "correct": "B"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["A. Charles Dickens", "B. William Shakespeare", "C. Jane Austen", "D. Mark Twain"],
        "correct": "B"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"],
        "correct": "D"
    }
]

score = 0

for q in questions:
    print(q["question"])
    for option in q["options"]:
        print(option)
    answer = input("Enter your answer (A, B, C, D): ").upper()
    if answer == q["correct"]:
        score += 1
        print("Correct! You win 100,000 rupees.\n")
    else:
        print("Wrong answer!\n")
        break

prize = score * 100000
print(f"You answered {score} questions correctly. Your total prize is {prize} rupees.")


# python3 projs/millionaire.py
