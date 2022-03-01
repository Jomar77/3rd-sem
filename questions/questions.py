class Question:
    def __init__(self):
        self.prompt = ""
        self.answer = ""

    def setText(self, prompt):
        self.prompt = prompt
    
    def setAnswer(self, answer):
        self.answer = answer
    
    def checkAnswer(self, response):
        return response == self.answer

    def displayPrompt(self):
        print(self.prompt)


class choiceQuestion(Question):
    def  __init__(self) :
        super().__init__()
        self._choices = []
    
    def  addChoice(self,  choice,  correct)  : 
        self._choices.append(choice) 
        if  correct  :
            choiceString  =  str(len(self._choices)) 
            self.setAnswer (choiceString)

    def  display(self) :
        super().displayPrompt()

        for  i  in  range(len(self._choices())): 
            choiceNumber  =  i  +  1 
            print("%d:  %s"  %  (choiceNumber, self._choices[i]))