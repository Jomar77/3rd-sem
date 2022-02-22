from letter import Letter

to = "John"
fro = "Mary"
line1 = "I am sorry we must part."
line2 = "I wish you all the best."

l = Letter(fro, to)
l.addLine(line1)
l.addLine(line2)



print(l.getText())
