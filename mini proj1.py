import random

score = 0

questions = [
    {
        "question": "What should you do first when you see a fire?",
        "options": ["A. Run away silently", "B. Call emergency services", "C. Hide", "D. Ignore it"],
        "answer": "B"
    },
    {
        "question": "Which habit helps maintain good health?",
        "options": ["A. Skipping meals", "B. Drinking enough water", "C. Sleeping very little", "D. Eating junk food daily"],
        "answer": "B"
    },
    {
        "question": "Why is saving money important?",
        "options": ["A. To spend it all later", "B. For future needs and emergencies", "C. To avoid work", "D. Only for rich people"],
        "answer": "B"
    },
    {
        "question": "Which of these helps protect the environment?",
        "options": ["A. Using plastic bags", "B. Wasting electricity", "C. Recycling waste", "D. Cutting trees"],
        "answer": "C"
    },
    {
        "question": "What is the safest way to cross a road?",
        "options": ["A. Running across", "B. Crossing anywhere", "C. Using a zebra crossing", "D. Looking at your phone"],
        "answer": "C"
    },
    {
        "question": "Which practice improves mental well-being?",
        "options": ["A. Constant stress", "B. Regular exercise", "C. No sleep", "D. Excess screen time"],
        "answer": "B"
    },
    {
        "question": "Why is teamwork important?",
        "options": ["A. It wastes time", "B. It creates conflict", "C. It helps achieve goals better", "D. It avoids responsibility"],
        "answer": "C"
    },
    {
        "question": "What should you do before sharing personal information online?",
        "options": ["A. Share quickly", "B. Check if the source is safe", "C. Ignore privacy", "D. Share with everyone"],
        "answer": "B"
    },
    {
        "question": "Which is a renewable source of energy?",
        "options": ["A. Coal", "B. Petrol", "C. Solar energy", "D. Diesel"],
        "answer": "C"
    },
    {
        "question": "What helps prevent the spread of diseases?",
        "options": ["A. Not washing hands", "B. Covering mouth while coughing", "C. Sharing utensils", "D. Ignoring hygiene"],
        "answer": "B"
    }
]

print("Welcome to the All-Ages Quiz!")
print("Answer by typing A, B, C, or D.\n")

random.shuffle(questions)

for i in range(5):
    q = questions[i]
    print(f"{i+1}. {q['question']}")
    for option in q["options"]:
        print(option)

    answer = input("Your answer: ").upper()

    if answer == q["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! Correct answer is {q['answer']}.\n")

print("Quiz Finished!")
print(f"Your final score: {score}/5")

if score == 5:
    print("Excellent knowledge! 🌟")
elif score >= 3:
    print("Good awareness! 👍")
else:
    print("Please try again! 💪")
