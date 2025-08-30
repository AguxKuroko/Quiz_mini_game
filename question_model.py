class Question:
    def __init__(self, question_text, answer):
        self.question_text = question_text
        self.answer = answer

    def __str__(self):
        return f"Question: {self.question_text}| Answer: {self.answer}"
    
