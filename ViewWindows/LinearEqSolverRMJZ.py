from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LinearEqSolverRMJZ(object):
    def setupUi(self, LinearEqSolverRMJZ):
        LinearEqSolverRMJZ.setObjectName("LinearEqSolverRMJZ")
        LinearEqSolverRMJZ.resize(511, 426)
        LinearEqSolverRMJZ.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        LinearEqSolverRMJZ.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.centralwidget = QtWidgets.QWidget(LinearEqSolverRMJZ)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label1")
        self.horizontalLayout.addWidget(self.label)

        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout2.setObjectName("horizontalLayout2")
        self.e = QtWidgets.QTextEdit(self.centralwidget)
        self.e.setObjectName("e")
        self.horizontalLayout2.addWidget(self.e)

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
        LinearEqSolverRMJZ.setCentralWidget(self.centralwidget)
        self.retranslateUi(LinearEqSolverRMJZ)
        QtCore.QMetaObject.connectSlotsByName(LinearEqSolverRMJZ)

    def retranslateUi(self, LinearEqSolverRMJZ):
        _translate = QtCore.QCoreApplication.translate
        LinearEqSolverRMJZ.setWindowTitle(_translate("LinearEqSolverRMJZ", "LinearEqSolverRMJZ"))
        self.label.setText(
            "Enter your equations: \n- Ex:2a+4y+6Z=5 \n- x,K1,nAme20 are considered variables but not x1x\n- Spaces are allowed\n- Write each equation in a new line\n- Press submit when your equations are ready\n- If you wish to change the nonLinearMethod or the precision, restart application")
        self.label.setStyleSheet(''' font-size: 16px; ''')
        self.e.setHtml(_translate("LinearEqSolverRMJZ",
                                  "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                  "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                  "p, li { white-space: pre-wrap; }\n"
                                  "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                  "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))

        self.Submit.setText(_translate("LinearEqSolverRMJZ", "Submit"))
        self.Back.setText(_translate("LinearEqSolverRMJZ", "Back to Previous"))
