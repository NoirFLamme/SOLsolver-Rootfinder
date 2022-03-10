import timeit
from collections import defaultdict
from PyQt5 import QtCore, QtWidgets
from ViewWindows.LinearEqSolverRMJZ import Ui_LinearEqSolverRMJZ
from HelpingMethods.LinearRegex import LinearRegex
from PyQt5.QtWidgets import QMessageBox



class LinearEqSolverBackend(QtWidgets.QMainWindow):
    nov = 2
    def __init__(self,inst):
        QtWidgets.QMainWindow.__init__(self)
        self.win = Ui_LinearEqSolverRMJZ()
        self.win.setupUi(self)
        self.mainInst = inst
        self.submitFlag123 = False
        self.submitFlag45 = False
        self.win.Submit.clicked.connect(self.submitPressed)
        self.win.Back.clicked.connect(self.backToPrev)
        self.matA = []
        self.matB = []
        self.win.Back.setDisabled(1)
        self.solVect = []


    def validate(self,mat):
        z = defaultdict(list)
        max = 0
        variables = {}
        x = sorted(mat)
        for i in x:
            for j in i:
                variables[j[2]] = 1

        for i in mat:
            duplicate = {}

            m = 0
            for j in i:
                m += 1
                if j[2] in duplicate.keys():
                    self.edyAlert("Equation " + str(i + 1) + " is invalid. Prevent repetition of variables.")
                    return False
                else:
                    duplicate[j[2]] = 1
            h = 0
            for key in variables.keys():
                if h < len(i):
                    if key == i[h][2]:
                        if i[h][0] != '-':
                            z[key].append(i[h][1])
                            print(1)
                        elif i[h][1] == '':
                            z[key].append("-1")
                            print(2)
                        else:
                            z[key].append("-" + i[h][1])
                            print(3)
                        h += 1
                    else:
                        z[key].append(0)
                        print(4)
                else:
                    z[key].append(0)
                    print(5)

            if (m > max):
                max = m
                print(8)
        if max > len(mat):
            self.edyAlert("Your equations have infinite number of solution. Thus, cannot be solved. Please re-enter.")
            return False
        dictZItems = dict(z).items()
        return sorted(dictZItems)

    def tab(self,mat, b):
        coeff = [[0] * len(mat) for i in range(len(mat[0][1]))]
        free = []
        y = 0
        for items in mat:
            x = 0
            for i in items[1]:
                if i != '':
                    coeff[x][y] = float(i)
                else:
                    coeff[x][y] = 1.0
                x += 1
            y += 1
        for i in b:
            free.append(float(i[0]))

        return coeff, free

    def edyAlert(self, text="Error"):
        msg = QMessageBox()
        msg.setWindowTitle("Alert")
        msg.setText(text)
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()  # this will show our messagebox

    def backToPrev(self):
        if self.submitFlag45:
            self.win.g.setParent(None)
            self.win.label2.setParent(None)
            try:
                self.win.timeLabel.setParent(None)
            except:
                pass
            self.win.e.setReadOnly(False)
            self.win.label.setText(
                "Enter your equations: \n- Ex:2a+4y+6Z=5 \n- x,K1,nAme20 are considered variables but not x1x\n- Spaces are allowed\n- Write each equation in a new line")
            self.win.label.setStyleSheet('''font-size:16px;''')
            self.win.Back.setDisabled(True)
            self.win.Submit.setDisabled(False)
            self.submitFlag45 = False
        if self.submitFlag123:
            for i in range (self.nov):
                self.win.labelz[i].setParent(None)
                self.win.timeLabel.setParent(None)
            if self.mainInst.is123:
                self.win.label.setText(
                    "Enter your equations: \n- Ex:2a+4y+6Z=5 \n- x,K1,nAme20 are considered variables but not x1x\n- Spaces are allowed\n- Write each equation in a new line")
                self.win.label.setStyleSheet('''font-size:16px;''')
                self.win.e.setReadOnly(False)
                self.win.Back.setDisabled(True)
            else:
                self.win.label.setText("Equations are entered!\nPress 'Back to Previous'\nif you want to edit.")
                self.win.label.setStyleSheet('''font-size:20px;''')
                self.win.g.setReadOnly(False)
            self.win.Submit.setDisabled(False)
            self.submitFlag123 = False



    def submitPressed(self):
        print(self.mainInst.method)
        if not self.submitFlag45:
            self.currText = self.win.e.toPlainText()
            self.currText = self.currText.replace(" ", "")
            print(self.currText)
            regexInst = LinearRegex()
            self.matA, self.matB = regexInst.parseMe(self.currText.splitlines())
            self.nov = len(self.matB)
            if not self.nov:
                return
            self.dic = self.validate(self.matA)
            if self.dic == False:
                return
            print(self.dic)
            self.matA, self.matB = self.tab(self.dic, self.matB)
            print(self.matA)
            print(self.matB)
            if not self.mainInst.is123:
                self.submitFlag45 = True
                self.win.e.setReadOnly(True)
                self.win.label2 = QtWidgets.QLabel(self.win.centralwidget)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.win.label2.sizePolicy().hasHeightForWidth())
                self.win.label2.setSizePolicy(sizePolicy)
                self.win.label2.setObjectName("label2")
                self.win.horizontalLayout.addWidget(self.win.label2)
                self.win.horizontalLayout.setStretch(0, 4)
                self.win.horizontalLayout.setStretch(1, 1)
                self.win.g = QtWidgets.QTextEdit(self.win.centralwidget)
                self.win.g.setObjectName("g")
                self.win.horizontalLayout2.addWidget(self.win.g)
                self.win.horizontalLayout2.setStretch(0, 6)
                self.win.horizontalLayout2.setStretch(1, 1)
                self.win.label2.setText(
                    "\n     Enter\n"
                    "     your\n    "
                    +    str(self.nov) + " initial\n "
                    "   guesses:")
                self.win.label2.setStyleSheet('''font-size:18px;''')
                self.win.label.setText("Equations are entered!\nPress 'Back to Previous'\nif you want to edit.")
                self.win.label.setStyleSheet('''font-size:20px;''')
                self.win.g.setText("0"+ (self.nov-1)*"\n0")
                self.win.Back.setDisabled(False)
                return

        if not self.mainInst.is123:
            self.win.g.setReadOnly(True)
            guessWhat = self.win.g.toPlainText()
            guessWhat = guessWhat.splitlines()
            if len(guessWhat) != self.nov:
                self.edyAlert("Number of guesses should be equal number of equations. Please re-enter.")
                return
            r = LinearRegex()
            guessValid = r.parseGuess(guessWhat)
            if not guessValid:
                self.edyAlert("Guesses are invlalid. Please re-enter.")
                return
            self.mainInst.setGuess(guessWhat)
        t1 = self.current_time()
        self.solVect,steps = self.mainInst.solve(self.matA,self.matB)
        if self.solVect==False:
            return
        t2 = self.current_time()
        self.time = round(float((t2-t1)*1000),4)
        self.showTime()
        print(self.time,"ms")
        print(steps)
        print(self.solVect)
        file = open("Saved Steps of Linear/Latest " + self.mainInst.method + " Steps.txt", "w")
        file.write(steps)
        file.close()
        self.showSol()
        self.submitFlag123 = True
        self.win.Back.setDisabled(False)
        self.win.Submit.setDisabled(True)


    def showSol(self):
        self.win.e.setReadOnly(True)
        self.win.Back.setDisabled(False)
        self.win.Submit.setDisabled(True)
        if not self.mainInst.is123:
            self.win.label.setText(
                "- Press back to previous to re-enter\n another set of equations\n- If you wish to change the method\n or the precision, restart application")
        else:
            self.win.label.setText(
            "- Press back to previous to re-enter another set of equations\n- If you wish to change the nonLinearMethod or the precision, restart application")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.win.hl = []
        self.win.labelz = []
        for i in range(0,self.nov,2):
            j = int(i/2)
            self.win.hl.append(QtWidgets.QHBoxLayout())
            self.win.hl[j].setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
            self.win.hl[j].setObjectName("hl" + str(i))
            self.win.labelz.append(QtWidgets.QLabel(self.win.centralwidget))
            sizePolicy.setHeightForWidth(self.win.labelz[i].sizePolicy().hasHeightForWidth())
            self.win.labelz[i].setSizePolicy(sizePolicy)
            self.win.labelz[i].setObjectName(self.dic[i][0])
            self.win.labelz[i].setAlignment(QtCore.Qt.AlignCenter)
            self.win.labelz[i].setText(str(self.dic[i][0]) + " = " + str(self.solVect[i]))
            self.win.labelz[i].setStyleSheet(''' font-size: 14px; ''')
            self.win.hl[j].addWidget(self.win.labelz[i])
            if i+1 < self.nov:
                self.win.labelz.append(QtWidgets.QLabel(self.win.centralwidget))
                self.win.labelz[i+1].setSizePolicy(sizePolicy)
                self.win.labelz[i+1].setObjectName(self.dic[i+1][0])
                self.win.labelz[i+1].setAlignment(QtCore.Qt.AlignCenter)
                self.win.labelz[i+1].setText(str(self.dic[i+1][0]) + " = " + str(self.solVect[i+1]))
                self.win.labelz[i+1].setStyleSheet(''' font-size: 14px; ''')
                self.win.hl[j].addWidget(self.win.labelz[i+1])
            self.win.verticalLayout.insertLayout(self.win.verticalLayout.count()-1,self.win.hl[j])

    def showTime(self):
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.win.hlLast = QtWidgets.QHBoxLayout()
        self.win.hlLast.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.win.hlLast.setObjectName("hlLast")
        self.win.timeLabel = QtWidgets.QLabel(self.win.centralwidget)
        sizePolicy.setHeightForWidth(self.win.timeLabel.sizePolicy().hasHeightForWidth())
        self.win.timeLabel.setObjectName("timeLabel")
        self.win.timeLabel.setSizePolicy(sizePolicy)
        self.win.timeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.win.timeLabel.setText("Runtime: " + str(self.time) + " ms")
        self.win.timeLabel.setStyleSheet(''' font-size: 16px; ''')
        self.win.hlLast.addWidget(self.win.timeLabel)
        self.win.verticalLayout.insertLayout(self.win.verticalLayout.count()-1,self.win.hlLast)


    def current_time(self):
        return timeit.default_timer()














