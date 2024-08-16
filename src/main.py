from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = [Question(ques['text'], ques['answer']) for ques in question_data]
quiz = QuizBrain(question_bank)

while quiz.has_next_question():
    quiz.next_question()
    print()

print(f"You have completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}.")
