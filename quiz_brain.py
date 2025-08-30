class QuizBrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        if self.question_number >= len(self.question_list):
            return False
        return True

    def next_question(self):
        q_question = self.question_list[self.question_number]
        question = f"Q{self.question_number+1}: {q_question.question_text} [True/False?]"
        self.question_number = self.question_number +1
        user_answer = input(f"{question}:\n")
        self.check_answer(user_answer,q_question.answer)



    def check_answer(self, user_answer, q_question):
        if user_answer.lower() == q_question.lower():
            print("Ding!Dong! Correct +1 point for you!")
            self.score +=1
        else:
            print("Buuuuu!Wrong!No point for you this round")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")







