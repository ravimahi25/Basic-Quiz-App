def run_quiz():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
            "answer": "C) Paris"
        },
        {
            "question": "What is 2 + 2?",
            "options": ["A) 3", "B) 4", "C) 5", "D) 6"],
            "answer": "B) 4"
        },
        {
            "question": "What is the largest ocean on Earth?",
            "options": ["A) Atlantic Ocean", "B) Indian Ocean", "C) Arctic Ocean", "D) Pacific Ocean"],
            "answer": "D) Pacific Ocean"
        },
        {
            "question": "What is the capital of Japan?",
            "options": ["A) Beijing", "B) Seoul", "C) Tokyo", "D) Bangkok"],
            "answer": "C) Tokyo"
        },
        {
            "question": "What is the chemical symbol for water?",
            "options": ["A) H2O", "B) CO2", "C) O2", "D) NaCl"],
            "answer": "A) H2O"
        }
    ]

    score = 0

    for index, question in enumerate(questions):   # enumerate allows us to get both the index and the question
        print(f"Question {index + 1}: {question['question']}")
        for option in question['options']:
            print(option)

        user_answer = input("Your answer (A/B/C/D): ")
        if user_answer.strip().upper() == question['answer'][0]:  # Compare only the first character (A/B/C/D)
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {question['answer']}\n")

    # These print statements are now outside the loop
    print(f"Your final score is: {score}/{len(questions)}")
    print("Thank you for playing!")

run_quiz()




