import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from FactoriesAndInterfaces.NonlinearInterface import NonlinearInterface

class Ui_NonlinearEqSolverRMJZ(object):
    def setupUi(self, NonlinearEqSolverRMJZ, inst):
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.mainInst = inst
        NonlinearEqSolverRMJZ.setObjectName("NonlinearEqSolverRMJZ")
        NonlinearEqSolverRMJZ.resize(511, 150)
        NonlinearEqSolverRMJZ.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        NonlinearEqSolverRMJZ.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.centralwidget = QtWidgets.QWidget(NonlinearEqSolverRMJZ)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacer = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout.addItem(spacer)
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setObjectName("label1")
        self.horizontalLayout.addWidget(self.label1)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        sizePolicy.setHeightForWidth(self.label1.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label1.setSizePolicy(sizePolicy)
        print(self.mainInst.method)
        if self.mainInst.is125:
            self.label2 = QtWidgets.QLabel(self.centralwidget)
            self.label2.setObjectName("label2")
            self.horizontalLayout.addWidget(self.label2)
            self.horizontalLayout.addItem(spacer)
            self.horizontalLayout.setStretch(0, 6)
            self.horizontalLayout.setStretch(2, 0)
            self.horizontalLayout.setStretch(3, 0)
            sizePolicy.setHeightForWidth(self.label2.sizePolicy().hasHeightForWidth())
            self.label2.setSizePolicy(sizePolicy)
        else:
            self.horizontalLayout.setStretch(0, 6)
            self.horizontalLayout.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout2.setObjectName("horizontalLayout2")
        self.e = QtWidgets.QLineEdit(self.centralwidget)
        self.e.setObjectName("e")
        self.horizontalLayout2.addWidget(self.e)
        self.g1 = QtWidgets.QLineEdit(self.centralwidget)
        self.g1.setObjectName("g2")
        self.horizontalLayout2.addWidget(self.g1)
        if self.mainInst.is125:
            self.g2 = QtWidgets.QLineEdit(self.centralwidget)
            self.g2.setObjectName("g2")
            self.horizontalLayout2.addWidget(self.g2)
            self.horizontalLayout2.setStretch(0, 6)
            self.horizontalLayout2.setStretch(1, 1)
            self.horizontalLayout2.setStretch(2, 1)
        else:
            self.horizontalLayout2.setStretch(0, 6)
            self.horizontalLayout2.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout2)
        self.horizontalLayout3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout3.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout3.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout3.setObjectName("horizontalLayout3")
        self.Back = QtWidgets.QPushButton(self.centralwidget)
        self.Back.setObjectName("Back")
        self.horizontalLayout3.addWidget(self.Back)
        self.Submit = QtWidgets.QPushButton(self.centralwidget)
        self.Submit.setObjectName("Submit")
        self.horizontalLayout3.addWidget(self.Submit)
        self.verticalLayout.addLayout(self.horizontalLayout3)
        NonlinearEqSolverRMJZ.setCentralWidget(self.centralwidget)
        self.retranslateUi(NonlinearEqSolverRMJZ)
        QtCore.QMetaObject.connectSlotsByName(NonlinearEqSolverRMJZ)

    def retranslateUi(self, NonlinearEqSolverRMJZ):
        _translate = QtCore.QCoreApplication.translate
        NonlinearEqSolverRMJZ.setWindowTitle(_translate("NonlinearEqSolverRMJZ", "NonlinearEqSolverRMJZ"))
        self.label.setText(
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
        self.label.setStyleSheet(''' font-size: 16px; ''')
        self.label1.setStyleSheet(''' font-size: 16px; ''')
        self.g1.setText(_translate("NonlinearEqSolverRMJZ","0"))
        try:
            self.label2.setStyleSheet(''' font-size: 16px; ''')
            self.g2.setText(_translate("NonlinearEqSolverRMJZ","1"))
        except:
            pass
        if self.mainInst.method == "Bisection" or self.mainInst.method == "False-Position":
            self.label1.setText(
                "\n\n\n\n\n\n\n\n\n\nLower"
                                  "\nBound:"
            )
            self.label2.setText(
                "\n\n\n\n\n\n\n\n\n\n   Upper"
                                  "\n   Bound:"
            )
        else:
            self.label1.setText(
                "\n\n\n\n\n\n\n\n\n\n     "
                                  "\nX0:  "
            )
            try:
                self.label2.setText(
                "\n\n\n\n\n\n\n\n\n\n         "  
                                  "\n      X1:"
                )
            except:
                pass
        self.Submit.setText(_translate("NonlinearEqSolverRMJZ", "Submit"))
        self.Back.setText(_translate("NonlinearEqSolverRMJZ", "Back to Previous"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    inst = NonlinearInterface("Secant",4,10,0.001)
    NonlinearEqSolverRMJZ = QtWidgets.QMainWindow()
    ui = Ui_NonlinearEqSolverRMJZ()
    ui.setupUi(NonlinearEqSolverRMJZ,inst)
    NonlinearEqSolverRMJZ.show()
    sys.exit(app.exec_())