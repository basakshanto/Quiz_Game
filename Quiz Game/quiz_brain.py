from data import question_data

TOTAL_QUESTIONS = len(question_data)


class QuizBrain:
    def __init__(self):
        self.question_list = []
        self.option_list = []
        self.answer_list = []
        self.score = 0
        self.question_number = 0
        self.count = 1

    def loading_question_to_list(self):
        for n in range(len(question_data)):
            new_question = question_data[n]["question"]
            self.question_list.append(new_question)

            multiple_choice = question_data[n]["choice"]
            self.option_list.append(multiple_choice)

            answer = question_data[n]["correct_answer"]
            self.answer_list.append(answer)

    def next_question(self):
        self.loading_question_to_list()
        current_question = self.question_list[self.question_number]
        current_option = self.option_list[self.question_number]

        print(f"\nQuestion {self.count}:\n{current_question}")
        for count in range(4):
            print(current_option[count])

        user_answer = input("\nYour answer: ").upper()
        self.checking_answer(user_answer)
        self.question_number += 1
        self.count += 1

    def checking_answer(self, user_answer):
        current_answer = self.answer_list[self.question_number].upper()
        if user_answer == current_answer:
            print("\nCorrect!")
            self.score += 1
        else:
            print("\nIncorrect!")

    def still_has_question(self):
        if self.count <= TOTAL_QUESTIONS:
            return True
