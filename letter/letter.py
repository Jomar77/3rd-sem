
class letter:

    def __init__(self, letterFrom, letterTo):
        self.letterFrom = letterFrom
        self.letterTo = letterTo

    def addLine(self, line):
        self.line = "Dear " + self.letterFrom + ":\n\n" + \
            line + "\n\nSincerely, \n\n" + self.letterTo

    def getLetter(self):
        return self.letter
    
    

    def getText(self):
        return self.line
