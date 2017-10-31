import pickle
import sys
from PyQt5.QtWidgets import (QMainWindow, QWidget, QGridLayout, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel, 
    QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        self.dbfilename = 'assignment6(1).dat'
        self.scoredb = []
        self.readScoreDB()
        # self.showScoreDB()
        
        
    def initUI(self):

        name = QLabel('Name: ')
        age = QLabel('Age: ')
        score = QLabel('Score: ')
        amount = QLabel('Amount: ')
        key = QLabel('Key: ')
        result = QLabel('Result: ')

        self.nameEdit = QLineEdit()
        self.ageEdit = QLineEdit()
        self.scoreEdit = QLineEdit()
        self.amountEdit = QLineEdit()
        self.resultWindow = QTextEdit()
        self.keyBox = QComboBox()
        self.keyBox.addItem('Name')
        self.keyBox.addItem('Age')
        self.keyBox.addItem('Score')

        addBtn = QPushButton("Add", self)
        delBtn = QPushButton("Del", self)
        findBtn = QPushButton("Find", self)
        incBtn = QPushButton("Inc", self)
        showBtn = QPushButton("Show", self)

        grid = QGridLayout()
        grid.setSpacing(1)

        grid.addWidget(name, 1, 1)
        grid.addWidget(self.nameEdit, 1, 3)
        grid.addWidget(age, 1, 4)
        grid.addWidget(self.ageEdit, 1, 5)
        grid.addWidget(score, 1, 6)
        grid.addWidget(self.scoreEdit, 1, 7)
        grid.addWidget(amount, 2, 4)
        grid.addWidget(self.amountEdit, 2, 5)
        grid.addWidget(key, 2, 6)
        grid.addWidget(self.keyBox, 2, 7)
        grid.addWidget(addBtn, 3, 3)
        grid.addWidget(delBtn, 3, 4)
        grid.addWidget(findBtn, 3, 5)
        grid.addWidget(incBtn, 3, 6)
        grid.addWidget(showBtn, 3, 7)
        grid.addWidget(result, 6, 1)
        grid.addWidget(self.resultWindow, 7, 1, 10, 7)

        addBtn.clicked.connect(self.addbtn_clicked)
        showBtn.clicked.connect(self.showbtn_clicked)
        delBtn.clicked.connect(self.delbtn_clicked)
        findBtn.clicked.connect(self.findbtn_clicked)
        incBtn.clicked.connect(self.incbtn_clicked)

        self.setLayout(grid)


        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')
        self.show()

    def addbtn_clicked(self):
        self.resultWindow.setText("")
        record = {'Name':self.nameEdit.text(), 'Age':int(self.ageEdit.text()), 'Score':int(self.scoreEdit.text())}
        self.scoredb.append(record)
        self.showScoreDB(self.scoredb)

    def showbtn_clicked(self):
        self.resultWindow.setText("")
        self.showScoreDB(self.scoredb)

    def delbtn_clicked(self):
        self.resultWindow.setText("")
        i = 0
        while i < len(self.scoredb):
            if self.scoredb[i]['Name'] == self.nameEdit.text():
                del(self.scoredb[i])
            else:
                i += 1

        self.showScoreDB(self.scoredb)

    def findbtn_clicked(self):
        self.resultWindow.setText("")
        arr = []
        for q in self.scoredb:
            if q['Name'] == self.nameEdit.text():
                arr.append(q)
                self.showScoreDB(arr)
                del(arr[0])

    def incbtn_clicked(self):
        self.resultWindow.setText("")
        for q in self.scoredb:
            if q['Name'] == self.nameEdit.text():
                q['Score'] += int(self.amountEdit.text())
        self.showScoreDB(self.scoredb)

    def closeEvent(self, event):

        self.writeScoreDB()


    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb = pickle.load(fH)
            for p in self.scoredb:
                p['Age'] = int(p['Age'])
                p['Score'] = int(p['Score'])
        except:
            print("Empty DB: ", self.dbfilename)
        else:
            print("Open DB: ", self.dbfilename)
        fH.close()
        return self.scoredb


    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self, scdb):
        for p in sorted(scdb, key=lambda person : person[self.keyBox.currentText()]):
            str1 = ""
            for attr in sorted(p):
                if attr == 'Name':
                    str1 += attr + "=" + p[attr] + "\t"   # self.resultWindow.append(attr + "=" + p[attr])
                elif attr == 'Age' or attr == 'Score':
                    str1 += attr + "=" + str(p[attr]) + "\t"     # self.resultWindow.append(attr + "=" + str(p[attr]))
            self.resultWindow.append(str1)
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())
