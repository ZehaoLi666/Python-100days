class QuizBrain:
    def __init__(self,queation_bank):
        self.question_number = 0 
        self.question_list = queation_bank
        self.score = 0 

    
    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {question.text}. (True/False)?:")     ### if you want to print the object in the class, you need use XXX.text 
        self.check_answer(user_answer,question.answer)

    def still_has_questions(self):
        number = len(self.question_list)
        if self.question_number < number  :
            return True 
        else:
            return False 
        
    def check_answer(self,user_answer,question.answer):
        if user_answer.lower() == question.answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")

        print(f"Your current score is: {self.score}/{self.question_number}.")


        
