from data import question_data
from question_model import QuestionModel
from quiz_brain import Quiz_Brain

question_bank = []
for item in question_data:
    question_text = item["text"]
    question_answer = item["answer"]
    new_question = QuestionModel(question_text, question_answer)
    question_bank.append(new_question)
"""
for question in question_bank:  
    print(question.text)
    print(question.answer)
"""

    
question = Quiz_Brain(question_bank)

while question.still_has_questions():
    question.next_question()
    
print("You've completed the quiz")
print(f"Your final score is : {question.score}/ {question.question_number}")