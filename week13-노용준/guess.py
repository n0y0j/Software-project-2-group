import re
class Guess:

    def __init__(self, word):
        self.numTries = 0
        self.secretWord = word
        self.guessedChars = []

        self.temp = []
        self.temp += "_"*len(self.secretWord) # self.currentStatus의 값을 쉽게 바꿀수 있게
                                              # 만든 더미 리스트

        self.count = 0 #self.guessedChars의 인덱스 값을 알기 위한 변수
        self.find = 0 #같은 알파벳이 2번이상 쓰이는 단어가 나올 경우
                      # 각 단어들의 인덱스값을 알기 위한 변수

        self.currentStatus = "_"*len(self.secretWord)


    def display(self):
        print("Current: " + self.currentStatus)
        print("Tries : " + str(self.numTries))
        print(self.guessedChars)


    def guess(self, character):
        lower = character.lower() # 입력받은 모든 값을 소문자로 바꿈

        if re.match('[a-z]',lower) : # a부터 z까지의 알파벳들만 if문을 통과할 수 있다.
            self.guessedChars += lower # self.guessedChars 에 알파벳들을 입력

            # 만약 self.guessdChars의 self.count번 째 인덱스가 self.secreWord안에 있다면 if문을 통과한다.
            if self.guessedChars[self.count] in self.secretWord:
                self.find = self.secretWord.find(lower) # self.secretWord에서 알파벳의 인덱스 값을 찾는다
                self.temp[self.find] = lower # 찾은 self.find의 정수를 더미 리스트의 인덱스 값으로하여 입력받은 알파벳을 삽입한다.
                self.currentStatus = "".join(self.temp) # 더미 리스트를 스트링으로 변환한다.

                # 만약 self.secreWord에 같은 알파벳이 두개 이상 존재하는 단어일시 실행된다.
                # find 메쏘드는 찾는 알파벳이 존재하지 않을 시 -1을 리턴하므로 범위를 아래처럼 잡아주었다.
                while (self.secretWord[self.find + 1:]).find(lower) != -1:
                    self.find = self.secretWord[self.find + 1:].find(lower) + self.find + 1
                    self.temp[self.find] = lower
                    self.currentStatus = "".join(self.temp)
                # 정상적으로 if 문이 실행되었을 때 self.count를 +1 하여 self.guessChars의 인덱스 값을 다음 입력받은 알파벳으로 출력한다.
                self.count += 1
            else:
                self.numTries += 1 # 목숨을 1줄인다.
                self.count += 1 # self.count를 +1 하여 self.guessChars의 인덱스 값을 다음 입력받은 알파벳으로 출력한다.
        else :
            print("Enter a valid alphabet.") # 알파벳을 입력핮 않았을 때 실행된다.

        if self.currentStatus == self.secretWord :
            return True
