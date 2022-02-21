from letter.letter import letter

to = "John"
fro = "Mary"
line1 = "I am sorry we must part."
line2 = "I wish you all the best."

l = letter(fro, to)
l.addLine(line1+'\n'+line2)


print(l.getText())
