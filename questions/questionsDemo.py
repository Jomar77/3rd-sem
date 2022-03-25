from questions import choiceQuestion

def main():
    first = choiceQuestion()
    first.setText("What is the capital of France?")
    first.addChoice("Paris", True)
    first.addChoice("London", False)
    first.addChoice("Berlin", False)
    first.addChoice("Madrid", False)

    second = choiceQuestion()
    second.setText("What is the capital of Germany?")
    second.addChoice("Paris", False)
    second.addChoice("London", False)
    second.addChoice("Berlin", True)
    second.addChoice("Madrid", False)

    third = choiceQuestion()
    third.setText("What is the capital of Spain?")
    third.addChoice("Paris", False)
    third.addChoice("London", False)
    third.addChoice("Berlin", False)
    
    fifth.addChoice("Berlin", False)

    questions = [first, second, third, fourth, fifth]
    for i in range(len(questions)):
        presentQuestion(questions[i])
    
    

def presentQuestion(q):
    q.display()
    response = input("Your answer: ")
    print(q.checkAnswer(response))

main()
