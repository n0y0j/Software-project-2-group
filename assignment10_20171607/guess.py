class Guess:

    def __init__(self, word):
        self.word = word #비밀 단어
        self.guessedChars = [] #예상했던 영어 단어
        self.secretWord = word #secret 단어
        self.answer = ["_"] * len(word) #비밀 단어를 담는 리스트
        self.failword = []
        self.numTries = 0  # 실패한 횟수 선언
        self.count = 0  # 실패한 횟수를 판별하기 위한 count
        self.failcount = 0


    def display(self):
        print("\n")
        for i in range(0, len(self.answer)):
            print(str(self.answer[i])+"  ", end = ' ')
        print("\n")

    def guess(self, character):
        for i in range(0, len(self.word)):
            if(self.word[i] == character):
                self.guessedChars.append(character)
                self.answer[i] = character
            else:
                self.failcount = self.failcount + 1
        if(self.failcount == len(self.word)):
            self.failword.append(character)
            self.numTries = self.numTries + 1
        self.failcount = 0
        while(self.count != len(self.word)):
            if(self.word[self.count] == self.answer[self.count]):
                self.count = self.count + 1
            else:
                break
        if(self.count == len(self.word)):
            return True
        else:
            return False



