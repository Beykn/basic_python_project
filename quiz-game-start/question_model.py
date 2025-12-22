class QuestionModel:
    def __init__(self, question_text, answer):
        self.text = question_text
        self.answer = answer
new_question = QuestionModel("Is the sky blue?", "True")
#print(new_question.text) 