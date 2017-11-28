class Guess:

    def __init__(self, word):

        self.secretWord = word
        self.numTries = 0
        self.guessedChars = []
        self.currentStatus = ""
        for i in range(len(word)):
            self.currentStatus += "_"




    def display(self):
        print("Current: " + self.currentStatus + "\n")
        print("Tries: " + str(self.numTries))



    def guess(self, character):
        self.guessedChars.append(character)
        if character not in self.secretWord:
            self.numTries += 1
        else:
            for i in range(len(self.currentStatus)):
                if character == self.secretWord[i]:
                    self.currentStatus = self.currentStatus[:i] + character + self.currentStatus[i+1:]




        for i in range(len(self.secretWord)):
            if self.currentStatus[i] == "_":
                return False
        return True

text = "_____"
text1 = text.replace(text[0], "a")
print(text1)