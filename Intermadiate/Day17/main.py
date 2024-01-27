from question_model import Question 
from data import question_data
from quiz_brain import QuizBrain


queation_bank = [] 


for items in question_data:
    question = Question(items["text"],items["answer"]) 
    queation_bank.append(question)


quiz = QuizBrain(queation_bank) 
quiz.next_question() 

while quiz.still_has_questions():
    quiz.next_question() 