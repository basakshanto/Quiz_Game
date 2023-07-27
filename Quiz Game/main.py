from quiz_brain import QuizBrain, TOTAL_QUESTIONS


def starting_quiz():
    print("Quiz Game")
    print("---------")
    print("1. Start Quiz")
    print("2. Exit")


starting_quiz()
quiz_brain = QuizBrain()

game_is_on = True

while game_is_on:
    user_choice = input("Enter your choice (1-2): ")
    if user_choice == "1":
        while quiz_brain.still_has_question():
            quiz_brain.next_question()

        print("Quiz Completed!")
        print("-------------------")
        print(f"Final Score: {quiz_brain.score}/{TOTAL_QUESTIONS}")
        print("\n1. Retry Quiz\n2. Exit")

        # Resetting everything
        quiz_brain.question_number = 0
        quiz_brain.count = 1
        quiz_brain.score = 0

    elif user_choice == "2":
        print("Exiting...")
        break

    else:
        print("\nInvalid input\n")

