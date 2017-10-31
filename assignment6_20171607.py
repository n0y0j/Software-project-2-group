import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication, QLabel,
                             QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()

    def initUI(self):
        lbl1 = QLabel("Name:", self)  # NAME LABEL
        self.nameEdit = QLineEdit("", self)  # NAME : LINE EDIT

        lbl2 = QLabel("Age:", self)
        self.ageEdit = QLineEdit("", self)

        lbl3 = QLabel("Score:", self)
        self.scoreEdit = QLineEdit("", self)

        box1 = QHBoxLayout()
        box1.addStretch(1)
        box1.addWidget(lbl1)
        box1.addWidget(self.nameEdit)
        box1.addWidget(lbl2)
        box1.addWidget(self.ageEdit)
        box1.addWidget(lbl3)
        box1.addWidget(self.scoreEdit)

        lbl4 = QLabel("Amount:", self)
        self.AtEdit = QLineEdit()

        lbl5 = QLabel("Key:", self)
        self.combo = QComboBox(self)
        self.combo.addItem("Age")
        self.combo.addItem("Name")
        self.combo.addItem("Score")

        box2 = QHBoxLayout()
        box2.addStretch(1)
        box2.addWidget(lbl4)
        box2.addWidget(self.AtEdit)
        box2.addWidget(lbl5)
        box2.addWidget(self.combo)

        self.btn1 = QPushButton("Add", self)
        self.btn1.clicked.connect(self.btn1_clicked)

        self.btn2 = QPushButton("Del", self)
        self.btn2.clicked.connect(self.btn2_clicked)

        self.btn3 = QPushButton("Find", self)
        self.btn3.clicked.connect(self.btn3_clicked)

        self.btn4 = QPushButton("Inc", self)
        self.btn4.clicked.connect(self.btn4_clicked)

        self.btn5 = QPushButton("show", self)
        self.btn5.clicked.connect(self.showScoreDB)

        self.btn6 = QPushButton("quit", self)
        self.btn6.clicked.connect(app.quit)

        box3 = QHBoxLayout()
        box3.addStretch(1)
        box3.addWidget(self.btn1)
        box3.addWidget(self.btn2)
        box3.addWidget(self.btn3)
        box3.addWidget(self.btn4)
        box3.addWidget(self.btn5)
        box3.addWidget(self.btn6)

        rult = QLabel("Result:")
        self.txtEdit = QTextEdit()
        box4 = QHBoxLayout()
        box4.addWidget(rult)
        box4.addWidget(self.txtEdit)

        vbox = QVBoxLayout()
        vbox.addLayout(box1)
        vbox.addLayout(box2)
        vbox.addLayout(box3)
        vbox.addLayout(box4)

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
            self.scoredb = pickle.load(fH)
            for record in self.scoredb:
                record['Score'] = int(record['Score'])
                record['Age'] = int(record['Age'])
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

    def showScoreDB(self):
        result = ""
        keyname = self.combo.currentText()
        for p in sorted(self.scoredb, key=lambda person: person[keyname]):
            for attr in sorted(p):
                result += str(attr) + "=" + str(p[attr]) + "\t"
            result += "\n"
            self.txtEdit.setPlainText(result)

    def btn1_clicked(self):  # add
        Name = self.nameEdit.text()
        Age = int(self.ageEdit.text())
        Score = int(self.scoreEdit.text())
        record = {'Name': Name, 'Age': Age, 'Score': Score}
        self.scoredb += [record]


    def btn2_clicked(self):  # del
        for i in range(len(self.scoredb)):
            for p in self.scoredb:
                if p['Name'] == self.nameEdit.text():
                    self.scoredb.remove(p)

    def btn3_clicked(self):  # findbutton
        result = ""
        for i in self.scoredb:
            if i['Name'] == self.nameEdit.text():
                for k, v in sorted(i.items()):
                    result += str(k) + "=" + str(v) + "\t"
                result += "\n"
                self.txtEdit.setPlainText(result)

    def btn4_clicked(self):  # incbutton
        for j in self.scoredb:
            if j['Name'] == self.nameEdit.text():
                a = int(j['Score']) + int(self.AtEdit.text())
                j['Score'] = a



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())