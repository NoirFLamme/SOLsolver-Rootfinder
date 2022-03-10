import sys
import timeit
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QImage, QPixmap

from FactoriesAndInterfaces.NonlinearInterface import NonlinearInterface
from ViewWindows.NonlinearEqSolverRMJZ import Ui_NonlinearEqSolverRMJZ
from HelpingMethods.NonlinearRegex import NonlinearRegex
from PyQt5.QtWidgets import QMessageBox
import cv2
from sympy import sympify




class NonlinearEqSolverBackend(QtWidgets.QMainWindow):
    def __init__(self,inst):
        QtWidgets.QMainWindow.__init__(self)
        self.win = Ui_NonlinearEqSolverRMJZ()
        self.win.setupUi(self,inst)
        self.mainInst = inst
        self.win.Submit.clicked.connect(self.submitPressed)
        self.win.Back.clicked.connect(self.backToPrev)
        self.win.Back.setDisabled(True)



    def edyAlert(self, text="Error"):
        msg = QMessageBox()
        msg.setWindowTitle("Alert")
        msg.setText(text)
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()  # this will show our messagebox

    def backToPrev(self):
        self.resize(511,150)
        self.win.timeLabel.setParent(None)
        self.win.solLabel.setParent(None)
        self.win.graphLabel.setParent(None)
        self.win.e.setReadOnly(False)
        self.win.g1.setReadOnly(False)
        try:
            self.win.g1.setReadOnly(False)
        except:
            pass
        self.win.label.setText(
            "Enter your expression:"
            "\n- Ex: x^4 - 3*x^3"
            "\n- Ex: cos(2*5*x^2) + exp(3*x)"
            "\n- Only lowercapsed x variable is allowed"
            "\n- Spaces are allowed and are not amust"
            "\n- paranthesis are amust with"
            "\n - sin(),cos(),tan(),exp()"
            "\n- A single EXPRESSION should be entered"
            "\n	- No equal signs are allowed"
            "\n- Press submit when ready"
            "\n- If you wish to change the method                      "
            "\n or the precision, restart application                  "
        )
        if self.mainInst.method == "Bisection" or self.mainInst.method == "False-Position":
            self.win.label1.setText(
                "\n\n\n\n\n\n\n\n\n\nLower"
                                  "\nBound:"
            )
            self.win.label2.setText(
                "\n\n\n\n\n\n\n\n\n\n   Upper"
                                  "\n   Bound:"
            )
        else:
            self.win.label1.setText(
                "\n\n\n\n\n\n\n\n\n\n     "
                                  "\nX0:  "
            )
            try:
                self.win.label2.setText(
                "\n\n\n\n\n\n\n\n\n\n         "  
                                  "\n      X1:"
                )
            except:
                pass
        self.win.label.setStyleSheet(''' font-size: 16px; ''')
        self.win.label.setStyleSheet('''font-size:16px;''')
        self.win.Back.setDisabled(True)
        self.win.Submit.setDisabled(False)



    def submitPressed(self):
        print(self.mainInst.method)
        currText = self.win.e.text()
        currText = currText.replace(" ", "")
        g1 = self.win.g1.text()
        print(currText)
        if currText == "":
            return
        regexInst = NonlinearRegex()
        if not regexInst.excute(currText) or not regexInst.parseGuess(g1):
            self.edyAlert("Invalid Input. Please re-read the rules and enter accordingly.")
            return
        g1 = float(g1)
        try:
            exp = sympify(currText)
        except:
            self.edyAlert("Invalid Input. Please re-read the rules and enter accordingly.")
            return
        if self.mainInst.is125:
            g2 = self.win.g2.text()
            if not regexInst.parseGuess(g2):
                self.edyAlert("Invalid Input. Please re-read the rules and enter accordingly.")
                return
            g2 = float(g2)
            self.mainInst.set2ndGuess(g2)
        t1 = self.current_time()
        self.solRoot,steps = self.mainInst.solve(exp,g1)
        if self.solRoot==False:
            return
        t2 = self.current_time()
        self.time = round(float((t2-t1)*1000),4)
        self.showTime()
        print(self.time,"ms")
        print(steps)
        print(self.solRoot)
        file = open("Saved Steps of Nonlinear/Latest " + self.mainInst.method + " Steps.txt", "w")
        file.write(steps)
        file.close()
        self.showSol()
        self.showGraph()
        self.win.Back.setDisabled(False)
        self.win.Submit.setDisabled(True)


    def showSol(self):
        self.win.e.setReadOnly(True)
        self.win.g1.setReadOnly(True)
        try:
            self.win.g2.setReadOnly(True)
        except:
            pass
        self.win.label.setStyleSheet('''font-size:20px;''')
        self.win.Back.setDisabled(False)
        self.win.Submit.setDisabled(True)
        self.win.label.setText(
            "- Press back to previous to re-enter\n another expression\n- If you wish to change the method\n or the precision, restart application")
        if self.mainInst.method == "Bisection" or self.mainInst.method == "False-Position":
            self.win.label1.setText(
                "\n\nLower"
                                  "\nBound:"
            )
            self.win.label2.setText(
                "\n\n   Upper"
                                  "\n   Bound:"
            )
        else:
            self.win.label1.setText(
                "\n\n     "
                                  "\nX0:  "
            )
            try:
                self.win.label2.setText(
                "\n\n         "  
                                  "\n      X1:"
                )
            except:
                pass
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.win.solHl = QtWidgets.QHBoxLayout()
        self.win.solHl.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.win.solHl.setObjectName("solHl")
        self.win.solLabel =QtWidgets.QLabel(self.win.centralwidget)
        sizePolicy.setHeightForWidth(self.win.solLabel.sizePolicy().hasHeightForWidth())
        self.win.solLabel.setSizePolicy(sizePolicy)
        self.win.solLabel.setObjectName("x")
        self.win.solLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.win.solLabel.setText(str("x = " + str(self.solRoot)))
        self.win.solLabel.setStyleSheet(''' font-size: 14px; ''')
        self.win.solHl.addWidget(self.win.solLabel)
        self.win.verticalLayout.insertLayout(self.win.verticalLayout.count()-1,self.win.solHl)

    def showGraph(self):
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.win.graphHl = QtWidgets.QHBoxLayout()
        self.win.graphHl.setObjectName("graphHl")
        self.win.graphLabel = QtWidgets.QLabel(self.win.centralwidget)
        sizePolicy.setHeightForWidth(self.win.graphLabel.sizePolicy().hasHeightForWidth())
        self.win.graphLabel.setSizePolicy(sizePolicy)
        self.win.graphLabel.setObjectName("graphLabel")
        self.win.graphHl.addWidget(self.win.graphLabel)
        self.win.verticalLayout.insertLayout(self.win.verticalLayout.count()-1,self.win.graphHl)
        graph = cv2.imread("Graphs of Nonlinear/Latest " + self.mainInst.method + " Graph.png")
        qformat = QImage.Format_Indexed8
        if len(graph.shape) == 3:
            if graph.shape[2] == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888
        outImage = QImage(graph, graph.shape[1], graph.shape[0], graph.strides[0], qformat)
        outImage = outImage.rgbSwapped()
        outImage = outImage.mirrored(False, False)
        self.win.graphLabel.setPixmap(QPixmap.fromImage(outImage))
        self.win.graphLabel.setScaledContents(True)


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

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    inst = NonlinearInterface("Bisection",4,10,0.001)
    NonlinearEqSolverRMJZ = QtWidgets.QMainWindow()
    ui = NonlinearEqSolverBackend(inst)
    ui.show()
    sys.exit(app.exec_())
