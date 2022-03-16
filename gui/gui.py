from tkinter import Canvas, Label, Tk, PhotoImage


root = Tk()
root.title("tk")

canvas = Canvas(root, width=400, height=400)

gif = PhotoImage(file="images/giphy.gif")
gif_lbl = Label(root, image=gif)
gif_lbl.grid (row=0, column=0)

text =  Label(text="Jomar A. Nacorda\n Davao City, April 13,2003", pady=10, padx=10, bg="light blue", fg="orange red", font=("Arial", 12))
text.grid(row=0, column=1)

root.mainloop()
