from fractions import Fraction


frac1 = Fraction(1, 8) # Stored as 1/8
frac2 = Fraction(-2, -4) # Stored as 1/2
frac3 = Fraction(-2, 4) # Stored as -1/2
frac4 = Fraction(3, -7) # Stored as -3/7
frac5 = Fraction(0, 15) # Stored as 0/1

for i in range (1, 6):
    print(i, ":", eval("frac" + str(i)))