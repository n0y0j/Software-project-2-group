import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):

    
    def __init__(self):
        super().__init__()
        

        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.ResultDisplay = QTextEdit()
        self.showScoreDB("Name")
        self.initUI()


        self.AddButton.clicked.connect(self.Do)
        self.FindButton.clicked.connect(self.Do)
        self.DelButton.clicked.connect(self.Do)
        self.IncButton.clicked.connect(self.Do)
        self.ShowButton.clicked.connect(self.Do)



        
        
    def initUI(self):

        Name = QLabel('Name:', self)
        Age = QLabel('Age:', self)
        Score = QLabel('Score', self)
        Amount = QLabel('Amount:', self)
        Key = QLabel('Key', self)
        self.KeySort = QComboBox(self)
        self.KeySort.addItem("Name")
        self.KeySort.addItem("Age")
        self.KeySort.addItem("Score")
        Result = QLabel('Result:', self)

        self.NameInput = QLineEdit()
        self.AgeInput = QLineEdit()
        self.ScoreInput = QLineEdit()
        self.AmountInput = QLineEdit()





        self.AddButton = QPushButton("Add")
        self.FindButton = QPushButton("Find")
        self.DelButton = QPushButton("Del")
        self.IncButton = QPushButton("Inc")
        self.ShowButton = QPushButton("Show")

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(Name)
        hbox.addWidget(self.NameInput)
        hbox.addWidget(Age)
        hbox.addWidget(self.AgeInput)
        hbox.addWidget(Score)
        hbox.addWidget(self.ScoreInput)

        hbox2 = QHBoxLayout()
        hbox.addStretch(1)
        hbox2.addWidget(Amount)
        hbox2.addWidget(self.AmountInput)
        hbox2.addWidget(Key)
        hbox2.addWidget(self.KeySort)

        hbox3 = QHBoxLayout()
        hbox.addStretch(1)
        hbox3.addWidget(self.AddButton)
        hbox3.addWidget(self.DelButton)
        hbox3.addWidget(self.FindButton)
        hbox3.addWidget(self.IncButton)
        hbox3.addWidget(self.ShowButton)

        hbox4 = QHBoxLayout()
        hbox.addStretch(1)
        hbox4.addWidget(Result)

        hbox5 = QHBoxLayout()
        hbox.addStretch(1)
        hbox5.addWidget(self.ResultDisplay)

        vbox = QVBoxLayout()
        vbox.addStretch(1)

        vbox.addLayout(hbox)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        vbox.addLayout(hbox5)




        self.setLayout(vbox)

        
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')
        self.show()


    def closeEvent(self, event):

        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb =  pickle.load(fH)
        except:
            pass
        else:
            pass

        fH.close()


    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self, keyname):
        count = 1
        temp = ""
        for p in sorted(self.scoredb, key=lambda person: person[keyname]) :
            if (count != 1) :
                temp += "\n"
            for attr in p:
                temp += attr + "=" + p[attr] +"\t"
                count+=1
        self.ResultDisplay.setText(temp)


    def Do(self):
        sender = self.sender()
        if (sender.text()=="Add") :
            if self.NameInput.text().isalpha() == True and self.AgeInput.text().isalpha()==False and self.ScoreInput.text().isalpha()==False :
                record = {'Name':self.NameInput.text(), 'Age':self.AgeInput.text(), 'Score':self.ScoreInput.text()}
                self.scoredb += [record]
                self.showScoreDB("Name")
            else :
                self.ResultDisplay.setPlainText("Error입니다." + "\n" +"Name,Int,Score의 InPut 값을 확인해주세요.")

        elif (sender.text()=="Find") :
            temp = ''
            count = 1
            for i in self.scoredb :
                if (i['Name'] == self.NameInput.text()) :
                    if (count != 1) :
                        temp += "\n"
                    for k,v in (i.items()) :
                        temp += k + "=" + v +'\t'
                        count += 1
                    self.ResultDisplay.setText(temp)

        elif (sender.text()=="Del") :
            for p in range(len(self.scoredb)) :
                for i in self.scoredb :
                    if (i['Name'] == self.NameInput.text()) :
                        self.scoredb.remove(i)
                        self.showScoreDB("Name")


        elif (sender.text()=="Inc") :
            for i in self.scoredb :
                if (i["Name"] == self.NameInput.text() and self.AmountInput.text().isalpha()==False) :
                    k = int(self.AmountInput.text()) + int(i["Score"])
                    i['Score'] = str(k)
                    self.showScoreDB("Name")


        else :
            if (self.KeySort.currentText()=="Name") :
                self.showScoreDB("Name")
            elif (self.KeySort.currentText() == "Age"):
                self.showScoreDB("Age")
            else :
                self.showScoreDB("Score")





        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())





