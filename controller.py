from PyQt5 import QtWidgets
from ViewWindows.EqSolverRMJZ import Ui_EqSolverRMJZ

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LinearEqSolverARMJZ = QtWidgets.QMainWindow()
    ui = Ui_EqSolverRMJZ()
    ui.setupUi(LinearEqSolverARMJZ)
    LinearEqSolverARMJZ.show()
    ui.userIn(LinearEqSolverARMJZ)
    sys.exit(app.exec_())

