from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []

for inx,data in enumerate(question_data):
    question_inx = Question(data['text'], data['answer'])
    question_bank.append(question_inx)

test = QuizBrain(question_bank)
while test.still_has_questions():
    test.next_question()
print("You completed the Quiz! Here is your final score",test.score)

