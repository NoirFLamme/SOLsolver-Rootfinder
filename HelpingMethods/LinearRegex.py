import re
from PyQt5.QtWidgets import QMessageBox


class LinearRegex:
    def __init__(self):
        self.pat1 = "([+-]?)(\d*\.?\d*)([a-zA-Z]+\d*)"
        self.pat2 = "=([-]?\d+\.?\d*)"
        self.pat3 = "([-]?\d+\.?\d*)"
        self.pat4 = "[a-zA-Z]+\d+[a-zA-Z]+"
        self.matA = []
        self.matB = []

    def checkVarName(self,eq):
        lol = re.compile(self.pat4)
        find = lol.finditer(eq)
        for j in find:
            if j.group(0) != eq:
                return False
        return True

    def parseGuess(self,g):
        for i in range (len(g)):
            lol = re.compile(self.pat3)
            find = lol.finditer(g[i])
            for j in find:
                if j.group(0) != g[i]:
                    return False
        return True

    def parseMe(self, eq):
        for i in range (len(eq)):
            if not self.checkVarName(eq[i]):
                self.edyAlert(i)
                continue
            if "=" not in eq[i]:
                self.edyAlert(i)
                continue
            detectMatrixA = re.compile(self.pat1)
            find1 = detectMatrixA.finditer(eq[i])
            eqCheck = ""
            for j in find1:
                eqCheck += j.group(0)
            checks1 = detectMatrixA.findall(eq[i])
            detectMatrixB = re.compile(self.pat2)
            find2 = detectMatrixB.finditer(eq[i])
            for j in find2:
                eqCheck += j.group(0)
            checks2 = detectMatrixB.findall(eq[i])
            print(eq[i])
            print(eqCheck)
            if eq[i]==eqCheck:
                self.matA.append(checks1)
                self.matB.append(checks2)
                continue
            self.edyAlert(i)
        print(self.matA)
        print(self.matB)
        return self.matA,self.matB

    def edyAlert(self,i):
        msg = QMessageBox()
        msg.setWindowTitle("Alert")
        msg.setText("Equation " + str(i + 1) + " is invalid. Please re-enter.")
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()  # this will show our messagebox
        self.matA.clear()
        self.matB.clear()

if __name__ == "__main__":
    ui = LinearRegex()
    #ui.parseMe(["4x+1.2y-16z=3","1.2x+.37y+43z=4.6","-1.6x-43y+98z=5.23"])
    val = ui.parseGuess(['12','-3.4','45','657','45','34','32','54','2'])
    #val = ui.checkVarName("joe+mono=1")
    print(val)



