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
    second.addChoice("Madrid", False)
    second.addChoice("Berlin", True)
    second.addChoice("London", False)

    third = choiceQuestion()
    third.setText("What is the capital of Italy?")
    third.addChoice("Paris", False)
    third.addChoice("Rome", True)
    third.addChoice("London", False)
    third.addChoice("Washington", False)
    

    fourth = choiceQuestion()
    fourth.setText("What is the capital of Spain?")
    fourth.addChoice("Paris", False)
    fourth.addChoice("Berlin", False)
    fourth.addChoice("Madrid", True)
    fourth.addChoice("London", False)

    fifth = choiceQuestion()
    fifth.setText("What is the capital of the United States?")
    fifth.addChoice("Paris", False)
    fifth.addChoice("Washington", True)
    fifth.addChoice("London", False)
    fifth.addChoice("Berlin", False)

    questions = [first, second, third, fourth, fifth]
    for i in range(len(questions)):
        presentQuestion(questions[i])
    
    

def presentQuestion(q):
    q.display()
    response = input("Your answer: ")
    print(q.checkAnswer(response))

main()
