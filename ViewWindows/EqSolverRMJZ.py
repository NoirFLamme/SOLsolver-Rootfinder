from PyQt5 import QtCore, QtGui, QtWidgets
from Components.LinearComponent import LinearEqSolverBackend
from Components.NonlinearComponent import NonlinearEqSolverBackend
from FactoriesAndInterfaces.LinearInterface import LinearInterface
from FactoriesAndInterfaces.LinearFactory import LinearFactory
from FactoriesAndInterfaces.NonlinearInterface import NonlinearInterface
from FactoriesAndInterfaces.NonlinearFactory import NonlinearFactory


class Ui_EqSolverRMJZ(object):
    selPrecision = 4
    isCb = 0
    isTb = 0
    isitr = 0
    islu = 0
    selectedMethod = "Gauss Elimination"
    method2 = None
    method2Value = None
    isLinear = True

    def setupUi(self, EqSolverRMJZ):
        EqSolverRMJZ.setObjectName("EqSolverRMJZ")
        EqSolverRMJZ.resize(563, 200)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(9)
        sizePolicy.setHeightForWidth(EqSolverRMJZ.sizePolicy().hasHeightForWidth())
        EqSolverRMJZ.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(EqSolverRMJZ)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.hl1 = QtWidgets.QHBoxLayout()
        self.hl1.setObjectName("hl1")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setObjectName("label1")
        self.hl1.addWidget(self.label1)
        self.eqNature = QtWidgets.QComboBox(self.centralwidget)
        self.eqNature.setObjectName("nonLinearMethod")
        self.eqNature.addItem("Linear")
        self.eqNature.addItem("Non-linear")
        self.hl1.addWidget(self.eqNature)
        self.verticalLayout.addLayout(self.hl1)
        self.goLinear()
        self.horizontalLayout23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout23.setObjectName("horizontalLayout23")
        self.horizontalLayout2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout2.setObjectName("horizontalLayout2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label2")
        self.horizontalLayout23.addWidget(self.label_2)
        self.Precision = self.createNumCombo("Precision", 4, 15)
        self.Precision.setCurrentIndex(11)
        self.horizontalLayout23.addWidget(self.Precision)
        self.Enter = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Enter.setFont(font)
        self.Enter.setObjectName("Enter")
        self.horizontalLayout23.addWidget(self.Enter)
        self.horizontalLayout23.setStretch(0, 4)
        self.horizontalLayout23.setStretch(1, 1)
        self.horizontalLayout23.setStretch(2, 6)
        self.verticalLayout.addLayout(self.horizontalLayout23)
        EqSolverRMJZ.setCentralWidget(self.centralwidget)
        self.retranslateUi(EqSolverRMJZ)
        QtCore.QMetaObject.connectSlotsByName(EqSolverRMJZ)

    def retranslateUi(self, LinearEqSolverARMJZ):
        _translate = QtCore.QCoreApplication.translate
        LinearEqSolverARMJZ.setWindowTitle(_translate("EqSolverRMJZ", "EqSolverRMJZ"))
        self.label1.setText(_translate("EqSolverRMJZ",
                                             "<html><head/><body><p><span style=\" font-size:14pt;\">State the nature of your equation(s):</span></p></body></html>"))
        self.eqNature.setItemText(0, _translate("EqSolverRMJZ", "Linear"))
        self.eqNature.setItemText(1, _translate("EqSolverRMJZ", "Non-linear"))
        self.eqNature.currentIndexChanged.connect(self.checkNature)
        self.label_2.setText(_translate("EqSolverRMJZ", "<html><head/><body><p><span style=\" font-size:14pt;\">Precision:</span></p></body></html>"))
        self.Enter.setText(_translate("EqSolverRMJZ", "Enter"))

    def createNumCombo(self,name,st,ed):
        _translate = QtCore.QCoreApplication.translate
        tempC = QtWidgets.QComboBox(self.centralwidget)
        tempC.setObjectName(name)
        j = 0
        for i in range (st,ed+1):
            tempC.addItem(str(i))
            tempC.setItemText(j, _translate("EqSolverRMJZ", str(i)))
            j+=1
        return tempC

    def radioCreate(self,name,layout,text):
        tempR = QtWidgets.QRadioButton(self.centralwidget)
        tempR.setObjectName(name)
        tempR.setText(QtCore.QCoreApplication.translate("EqSolverRMJZ",text))
        layout.addWidget(tempR)
        self.verticalLayout.insertLayout(self.verticalLayout.count() - 1, layout)
        return tempR

    def checkNature(self):
        nature = str(self.eqNature.currentText())
        if nature=="Linear":
            if not self.isLinear:
                self.nonLinearLabel1.setParent(None)
                self.nonLinearMethod.setParent(None)
                self.iterationLabel.setParent(None)
                self.ARELabel.setParent(None)
                self.itNoTb.setParent(None)
                self.ARETb.setParent(None)
                self.goLinear()
                self.isLinear = True
        else:
            if self.isLinear:
                self.linearLabel1.setParent(None)
                self.linearMethod.setParent(None)
                if self.isitr:
                    self.isARE.setParent(None)
                    self.isIteration.setParent(None)
                    if self.isTb:
                        self.itNoTb.setParent(None)
                        self.isTb = 0
                    elif self.isCb:
                        self.ARECb.setParent(None)
                        self.isCb = 0
                    self.isitr = 0
                if self.islu:
                    self.doLittle.setParent(None)
                    self.crout.setParent(None)
                    self.cholesky.setParent(None)
                    self.islu = 0
                self.isLinear = False
                self.goNonlinear()

    def goNonlinear(self):
        _translate = QtCore.QCoreApplication.translate
        self.nonLinearHL1 = QtWidgets.QHBoxLayout()
        self.nonLinearHL1.setObjectName("nonLinearHL1")
        spacer = QtWidgets.QSpacerItem(20, 3, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        self.nonLinearHL1.addSpacerItem(spacer)
        self.nonLinearLabel1 = QtWidgets.QLabel(self.centralwidget)
        self.nonLinearLabel1.setObjectName("label1")
        self.nonLinearHL1.addWidget(self.nonLinearLabel1)
        self.nonLinearMethod = QtWidgets.QComboBox(self.centralwidget)
        self.nonLinearMethod.setObjectName("nonLinearMethod")
        self.nonLinearMethod.addItem("Bisection")
        self.nonLinearMethod.addItem("False-Position")
        self.nonLinearMethod.addItem("Fixed-Point")
        self.nonLinearMethod.addItem("Newton Raphson")
        self.nonLinearMethod.addItem("Secant")
        self.nonLinearHL1.addWidget(self.nonLinearMethod)
        self.verticalLayout.insertLayout(1, self.nonLinearHL1)
        self.nonLinearLabel1.setText(_translate("EqSolverRMJZ",
                                             "<html><head/><body><p><span style=\" font-size:12pt;\">Choose nonLinearMethod of calculation:</span></p></body></html>"))
        self.nonLinearMethod.setItemText(0, _translate("EqSolverRMJZ", "Bisection"))
        self.nonLinearMethod.setItemText(1, _translate("EqSolverRMJZ", "False-Position"))
        self.nonLinearMethod.setItemText(3, _translate("EqSolverRMJZ", "Fixed-Point"))
        self.nonLinearMethod.setItemText(2, _translate("EqSolverRMJZ", "Newton Raphson"))
        self.nonLinearMethod.setItemText(4, _translate("EqSolverRMJZ", "Secant"))
        self.itHL = QtWidgets.QHBoxLayout()
        self.itHL.setObjectName("itHL")
        spacer = QtWidgets.QSpacerItem(40, 3, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        self.itHL.addSpacerItem(spacer)
        self.iterationLabel = QtWidgets.QLabel(self.centralwidget)
        self.iterationLabel.setObjectName("iterationLabel")
        self.itHL.addWidget(self.iterationLabel)
        self.itNoTb = QtWidgets.QLineEdit(self.centralwidget)
        self.itNoTb.setObjectName("itNoTb")
        self.itNoTb.setText("50")
        spacer2 = QtWidgets.QSpacerItem(200, 100, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        self.itHL.addSpacerItem(spacer2)
        self.itHL.addWidget(self.itNoTb)
        self.verticalLayout.insertLayout(self.verticalLayout.count()-1,self.itHL)
        self.AREHL = QtWidgets.QHBoxLayout()
        self.AREHL.setObjectName("AREHL")
        self.AREHL.addSpacerItem(spacer)
        self.ARELabel = QtWidgets.QLabel(self.centralwidget)
        self.ARELabel.setObjectName("ARELabel")
        self.AREHL.addWidget(self.ARELabel)
        self.ARETb = QtWidgets.QLineEdit(self.centralwidget)
        self.ARETb.setObjectName("itNoTb")
        self.ARETb.setText("0.0001")
        self.AREHL.addSpacerItem(spacer2)
        self.AREHL.addWidget(self.ARETb)
        self.verticalLayout.insertLayout(self.verticalLayout.count()-1,self.AREHL)
        self.iterationLabel.setText(_translate("EqSolverRMJZ", "<html><head/><body><p><span style=\" font-size:10pt;\">Enter maximam number of iterations:</span></p></body></html>"))
        self.ARELabel.setText(_translate("EqSolverRMJZ", "<html><head/><body><p><span style=\" font-size:10pt;\">Enter error tolerance:</span></p></body></html>"))


    def goLinear(self):
        _translate = QtCore.QCoreApplication.translate

        self.linearHL1 = QtWidgets.QHBoxLayout()
        self.linearHL1.setObjectName("linearHL")
        spacer = QtWidgets.QSpacerItem(20, 3, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        self.linearHL1.addSpacerItem(spacer)
        self.linearLabel1 = QtWidgets.QLabel(self.centralwidget)
        self.linearLabel1.setObjectName("label1")
        self.linearHL1.addWidget(self.linearLabel1)
        self.linearMethod = QtWidgets.QComboBox(self.centralwidget)
        self.linearMethod.setObjectName("nonLinearMethod")
        self.linearMethod.addItem("Gauss Elimination")
        self.linearMethod.addItem("Gauss Jordon")
        self.linearMethod.addItem("LU Decomposition")
        self.linearMethod.addItem("Gauss Siedel")
        self.linearMethod.addItem("Jacobi Iteration")
        self.linearHL1.addWidget(self.linearMethod)
        self.verticalLayout.insertLayout(1,self.linearHL1)
        self.linearLabel1.setText(_translate("EqSolverRMJZ", "<html><head/><body><p><span style=\" font-size:12pt;\">Choose nonLinearMethod of calculation:</span></p></body></html>"))
        self.linearMethod.setItemText(0, _translate("EqSolverRMJZ", "Gauss Elimination"))
        self.linearMethod.setItemText(1, _translate("EqSolverRMJZ", "Gauss Jordon"))
        self.linearMethod.setItemText(3, _translate("EqSolverRMJZ", "LU Decomposition"))
        self.linearMethod.setItemText(2, _translate("EqSolverRMJZ", "Gauss Siedel"))
        self.linearMethod.setItemText(4, _translate("EqSolverRMJZ", "Jacobi Iteration"))
        self.linearMethod.currentIndexChanged.connect(self.checkMethod)


    def checkMethod(self):
        self.selectedMethod = str(self.linearMethod.currentText())
        if (self.selectedMethod == "Gauss Siedel" or self.selectedMethod == "Jacobi Iteration"):
            self.Enter.setDisabled(1)
            if self.islu:
                self.doLittle.setParent(None)
                self.crout.setParent(None)
                self.cholesky.setParent(None)
                self.islu = 0
            if not self.isitr:
                self.itHL = QtWidgets.QHBoxLayout()
                self.itHL.setObjectName("itHL")
                spacer = QtWidgets.QSpacerItem(40, 3, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
                self.itHL.addSpacerItem(spacer)
                self.isIteration = self.radioCreate("isIteration",self.itHL,"Set number of iterations:")
                self.AREHL = QtWidgets.QHBoxLayout()
                self.AREHL.setObjectName("AREHL")
                self.AREHL.addSpacerItem(spacer)
                self.isARE = self.radioCreate("isARE", self.AREHL, "Set number of needed accuracy precision:")
            self.isIteration.clicked.connect(self.takeItNo)
            self.isARE.clicked.connect(self.takeARE)
            self.isitr = 1


        elif self.selectedMethod == "LU Decomposition" and not self.islu:
            self.Enter.setDisabled(1)
            self.islu = 1
            if self.isitr:
                self.isARE.setParent(None)
                self.isIteration.setParent(None)
                if self.isTb:
                    self.itNoTb.setParent(None)
                    self.isTb = 0
                elif self.isCb:
                    self.ARECb.setParent(None)
                    self.isCb = 0
                self.isitr = 0
            self.luCont = QtWidgets.QVBoxLayout()
            self.doLittleHl = QtWidgets.QHBoxLayout()
            spacer = QtWidgets.QSpacerItem(40, 3, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
            self.doLittleHl.addSpacerItem(spacer)
            self.doLittleHl.setObjectName("doLittleHl")
            self.doLittle = self.radioCreate("dolittle", self.doLittleHl,
                                                "Dolittle Form")

            self.croutHl = QtWidgets.QHBoxLayout()
            self.croutHl.setObjectName("croutHl")
            self.croutHl.addSpacerItem(spacer)
            self.crout = self.radioCreate("crout", self.croutHl,
                                               "Crout Form")

            self.choleskyHl = QtWidgets.QHBoxLayout()
            self.choleskyHl.setObjectName("choleskyHl")
            self.choleskyHl.addSpacerItem(spacer)
            self.cholesky = self.radioCreate("cholesky", self.choleskyHl,
                                               "Cholesky Form")
            self.doLittle.clicked.connect(lambda: self.passDolittle(self.doLittle.objectName()))
            self.crout.clicked.connect(lambda: self.passCrout(self.crout.objectName()))
            self.cholesky.clicked.connect(lambda: self.passCholesky(self.cholesky.objectName()))

        else:
            self.Enter.setDisabled(0)
            if self.isitr:
                self.isARE.setParent(None)
                self.isIteration.setParent(None)
                if self.isTb:
                    self.itNoTb.setParent(None)
                    self.isTb = 0
                elif self.isCb:
                    self.ARECb.setParent(None)
                    self.isCb = 0
                self.isitr = 0
            if self.islu:
                self.doLittle.setParent(None)
                self.crout.setParent(None)
                self.cholesky.setParent(None)
                self.islu = 0

    def passDolittle(self,meth2):
        self.Enter.setDisabled(0)
        self.method2 = meth2


    def passCrout(self,meth2):
        self.Enter.setDisabled(0)
        self.method2 = meth2


    def passCholesky(self,meth2):
        self.Enter.setDisabled(0)
        self.method2 = meth2



    def takeItNo(self):
        self.Enter.setDisabled(0)
        iterationsCount = 10
        if self.isTb:
            return
        if self.isCb:
            self.ARECb.setParent(None)
            self.isCb = 0
        self.itNoTb = QtWidgets.QLineEdit(self.centralwidget)
        self.itNoTb.setObjectName("itNoTb")
        self.itNoTb.setText(str(iterationsCount))
        spacer = QtWidgets.QSpacerItem(200, 100, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        self.itHL.addSpacerItem(spacer)
        self.itHL.addWidget(self.itNoTb)
        self.isTb = 1
        self.method2 = "isIteration"



    def takeARE(self):
        self.Enter.setDisabled(0)
        if self.isCb:
            return
        if self.isTb:
            self.itNoTb.setParent(None)
            self.isTb = 0
        spacer = QtWidgets.QSpacerItem(200, 100, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        self.AREHL.addSpacerItem(spacer)
        self.ARECb = self.createNumCombo("ARECb", 2, 10)
        self.AREHL.addWidget(self.ARECb)
        self.isCb = 1
        self.method2 = "isARE"

    def userIn(self, mainWindowInstance):
        self.Enter.clicked.connect(lambda: self.enterPressed(mainWindowInstance))

    def enterPressed(self, mainWindowInstance):
        self.selPrecision = int(self.Precision.currentText())
        self.openLinearWindow() if self.isLinear else self.openNonlinearWindow()
        mainWindowInstance.hide()

    def openLinearWindow(self):
        solInst = self.carryToLinearWindow()
        self.runLinearEqSolverRMJZ = LinearEqSolverBackend(solInst)
        self.runLinearEqSolverRMJZ.show()

    def carryToLinearWindow(self):
        if self.isCb:
            self.method2Value = int(self.ARECb.currentText())
        if self.isTb:
            self.method2Value = int(self.itNoTb.text())

        inst = LinearInterface(self.selectedMethod, self.selPrecision, self.method2, self.method2Value)
        fac = LinearFactory()
        return fac.use(inst)

    def openNonlinearWindow(self):
        solInst = self.carryToNonlinearWindow()
        self.runLinearEqSolverRMJZ = NonlinearEqSolverBackend(solInst)
        self.runLinearEqSolverRMJZ.show()

    def carryToNonlinearWindow(self):
        iterationsNum = int(self.itNoTb.text())
        self.selectedMethod = str(self.nonLinearMethod.currentText())
        eps = float(self.ARETb.text())
        inst = NonlinearInterface(self.selectedMethod, self.selPrecision, iterationsNum, eps)
        fac = NonlinearFactory()
        return fac.use(inst)

























