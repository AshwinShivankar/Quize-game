class QuizBrain:
    def __init__(self, question_list):
        self.question_no = 0
        self.question_list = question_list
        self.score = 0


    def still_has_questions(self):
        return self.question_no < len(self.question_list)

    def next_question(self, ):
        current_q = self.question_list[self.question_no]
        self.question_no += 1
        user_ans = input(f"Q.{self.question_no}: {current_q.text} (true,false): ")
        self.check_answer(user_ans, current_q.answer)

    def check_answer(self, user_ans, correct_ans):
        if user_ans.lower() == correct_ans:
            self.score += 1

            print("You got it right")
        else:
            self.score -= 1
            print("That's Wrong")
        print(f"The correct answer was {correct_ans}")
