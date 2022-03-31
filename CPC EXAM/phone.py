from tkinter import END, RIGHT, Button, Entry, Frame, Tk

root = Tk()

# sets the name on the top of the gui
root.title("phone")

# fixed the width and height of the gui, so it can't be expanded
root.resizable(width=False, height=False)

# act as a container for numbers and symbols
calc = Frame(root)

# create a grid like pattern of the frame
calc.grid()

class enter():
    def __init__(self):
        self.current = ''
        self.input_value = True
        self.result = False

    def numberEnter(self, num):
        self.result = False
        firstnum = txtDisplay.get()
        secondnum = str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value = False
        else:
            self.current = firstnum+secondnum
        self.display(self.current)

    def display(self, value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)

added_value = enter()
# create a button for each number
txtDisplay = Entry(calc,
                   font=('Cebtury Gothic', 20,
                         'bold'),
                   bg='black',
                   fg='white',
                   bd=30,
                   width=16,
                   justify=RIGHT)
txtDisplay.grid(row=0,
                column=0,
                columnspan=3)

txtDisplay.insert(0, "0")

numberpad = "123456789*0#"

# here i will count the rows for placing buttons
i = 0

# create an empty list to store the buttons
btn = []

for j in range(2, 6):
    for k in range(3):
        # create a button for each number
        btn.append(Button(calc,
                          width=5,
                          height=2,
                          bg='white',
                          fg='black',
                          font=('Century Gothic', 20, 'bold'),
                          bd=4, text=numberpad[i]))

        # set buttons in row & column and separate them with a padding of 1 unit
        btn[i].grid(row=j, column=k, pady=1)

        # put that number as a symbol on that button
        btn[i]["command"] = lambda x=numberpad[i]: added_value.numberEnter(x)

        # increment the numberpad
        i += 1

root.mainloop()

'''
Contributed:
Jomar A. Nacorda
Hannah Gwyneth Valeroso
Jaye Martin Chan

Did not contribute:
Neph Ricard E. Arancon Jr.
Chass Clayton C. Estomo
'''