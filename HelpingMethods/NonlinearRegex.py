import re
from PyQt5.QtWidgets import QMessageBox

class NonlinearRegex:
    def __init__(self):
        scte = "(sin\(|cos\(|tan\(|exp\()*"
        self.checkPure = "[+-]?((([-]?\d*\.?\d*\*)*(\^[-]?\d*\.?\d*)?"+scte+"([-]?\d+\.?\d*)\)*)+|("+scte+"([-]?\d*\.?\d*\*)*"+scte+"x(\^[-]?\d*\.?\d*)?\)*(\^\[-]?d*\.?\d*)?)+)"
        self.oneNum = "([-]?\d+\.?\d*)"

    def parseGuess(self,g):
        lol = re.compile(self.oneNum)
        find = lol.finditer(g)
        for j in find:
            if j.group(0) != g:
                return False
            return True

    def checkParanthesis(self,exp):
        stack = []
        for i in exp:
            if i=="(":
                stack.append(i)
            elif i==")":
                try:
                    stack.pop()
                except:
                    return False
        if len(stack):
            return False
        return True

    def validate(self, exp):
        detectMatrixA = re.compile(self.checkPure)
        find1 = detectMatrixA.finditer(exp)
        expCheck = ""
        for j in find1:
            expCheck += j.group(0)
        print(exp)
        print(expCheck)
        if exp==expCheck:
            return True
        self.edyAlert()
        return False

    def excute(self,exp):
        if not self.checkParanthesis(exp):
            return False
        if not self.validate(exp):
            return False
        return True

    def edyAlert(self):
        msg = QMessageBox()
        msg.setWindowTitle("Alert")
        msg.setText("Expression is invalid. Please re-enter.")
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()  # this will show our messagebox

if __name__ == "__main__":
    ui = NonlinearRegex()
    val = ui.excute("5*-3*sin(-3)*cos(x^-2)^6+sin(x^3.4-3.4*x+4*x^6+6.64+3*sin(x)*exp(3))^7")
    # val = ui.excute("cos(x)*sin(3x^2)+exp(3*x)-2")
    print(val)

# 1 ... x ... 2*x ... x^2 ... 3*x^4
#sin(x) ... sin(1) ... sin(2*X) ... sin(x^2) ... sin(3*x^4) ... sin(AllPlused)
#sin(x) ... 3*sin(x)
#sin(x)^2 (NOT YET)
#sin(x)*cos(x)*tan(x) (NOT YET)
