# Quiz questions (can be moved to a JSON file for scalability)
quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["1. Paris", "2. London", "3. Berlin", "4. Madrid"],
        "answer": "1"
    },
    {
        "question": "What is the value of pi (approximately)?",
        "options": ["1. 2.14", "2. 3.14", "3. 4.14", "4. 5.14"],
        "answer": "2"
    },
    {
        "question": "Which planet is closest to the Sun?",
        "options": ["1. Venus", "2. Mars", "3. Mercury", "4. Earth"],
        "answer": "3"
    }
]


# Function to run the quiz
def run_quiz():

    print("Welcome to the Quiz!")
    print("Answer the following questions by typing the number of your choice.\n")


    score = 0

    for index, question_data in enumerate(quiz_data, start = 1):
        print(f"Question {index}: {question_data['question']}")

        for option in question_data['options']:
            print(option)

        while True:
            user_answer = input("Your answer: ").strip()

            if user_answer.isdigit() and int(user_answer) in range(1, len(question_data['options']) + 1):
                break
            else:
                print("Invalid input. Please enter a number from the list of options.")

        if user_answer == question_data["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! Correct answer: {question_data['answer']}\n")

    # Show final results
    print(f"Quiz Complete! Your total score is {score}/{len(quiz_data)}")
    if score == len(quiz_data):
        print("Excellent job!")
    elif score > len(quiz_data) // 2:
        print("Good effort!")
    else:
        print("Try harder next time!")


# Run the quiz
run_quiz()