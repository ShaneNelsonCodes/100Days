from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)

q_brain = QuizBrain(q_list=question_bank)

while q_brain.still_has_questions() == True:
    q_brain.next_question()

print("You've completed the quiz")
print(f"Your final score was: {q_brain.score}/{q_brain.question_number}")