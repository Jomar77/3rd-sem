def __init__(self, numerator=0, denominator=1):
    if denominator == 0:
        raise ZeroDivisionError("Denominator cannot be zero.")
    if numerator == 0:
        self._numerator  = 0
        self._denominator = 1
    else:
        if (numerator < 0 and denominator >= 0 or numerator >= 0 and denominator < 0):
            sign = -1
        else:
            sign = 1

    a = abs(numerator)
    b = abs(denominator)
    while a % b != 0 :
        tempA = a
        tempB = b
        a = tempB
        b = tempA % tempB
    self._numerator = abs(numerator) # b * sign
    self._denominator = abs(denominator)
