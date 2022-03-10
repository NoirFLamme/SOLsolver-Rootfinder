from PyQt5.QtWidgets import QMessageBox

from HelpingMethods import Print,pivot
from FactoriesAndInterfaces.LinearInterface import LinearInterface

class GaussSeidel:

    stepSolution = ""
    guess = []

    def __init__(self, obj):
        self.method = obj.method
        self.is123 = obj.is123
        self.precision = obj.precision
        self.method2 = obj.method2
        self.method2Value = obj.method2Value

    def edyAlert(self, text="Error"):
        msg = QMessageBox()
        msg.setWindowTitle("Alert")
        if text == "inf":
            msg.setText("Your equations have infinite number of solutions. Thus, cannot be solved. Please re-enter.")
        elif text == "noSol":
            msg.setText("Your equations have no soluion. Please re-enter.")
        else:
            msg.setText(text)
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()  # this will show our messagebox
        pass

    def testConverge(self,mat):         # test if matrix of coefficient diagonally dominant
        for i in range(len(mat)):
            Sum = sum(mat[i])           # get sum of each row
            dig = mat[i][i]             #element on main diagonal
            if dig < Sum - dig:         #
                return "may div"        # element on main diagonal should be at least equal
            else:                       # the sum of other elements
                continue                # other wise matrix may diverge
        return "con"                    #

    def setGuess(self,g):
        for i in range(len(g)):
            self.guess.append(float(g[i]))

    def solve(self, a, b):                                                                     # instantiate parameters
        self.coList = list(a)
        self.equal = b
        self.stepSolution = "Coefficient Matrix:\n"
        self.stepSolution += Print.writematrix(self.coList)
        self.stepSolution += "Free Terms Vector:\n" + Print.writevector(self.equal)
        self.stepSolution += "Initial Guess Vector:\n" + Print.writevector(self.guess)
        if self.method2 == "isIteration":                                                       #
            self.numOfIteration = int(self.method2Value)                                        #choose nonLinearMethod to solve
            Sol, steps = self.solveUsingIteration()                                             # solve using num of iterations
        else:                                                                                   #
            self.absoluteError = 0.5 * 10 ** (2 - int(self.method2Value))                       # get absolute relative error
            Sol, steps = self.solveUsingrelative()                                              # solve using absolute relative error
            print(steps)                                                                        #
        return Sol,steps

    def solveUsingIteration(self):                                                                  #
        n = len(self.coList)
        if det(self.coList) == 0:

            # Performs Gaussian Elimination to check whether it has an Infinite Solution or No Solution
            for i in range(0, n):
                for j in range(i + 1, n):
                    multiplier = round(self.coList[j][i] / (self.coList[i][i]), self.precision)
                    for k in range(i, n):
                        self.coList[j][k] = round(self.coList[j][k] + round(-multiplier * self.coList[i][k],
                                                                            self.precision),
                                                  self.precision)  # Use Multiplier to eliminate rows under pivot
                self.equal[j] = round(self.equal[j] + round(-multiplier * self.equal[i], self.precision))

            # Checks if a system has No solution
            for i in range(0, n):
                if self.coList[i][i] == 0 and self.equal[i] != 0:
                    self.stepSolution = "No Solution\n"
                    self.edyAlert("noSol")
                    return False, self.stepSolution

            # Else it has Infinite Solution
            self.stepSolution = "Infinite Solution\n"
            self.edyAlert("inf")
            return False, self.stepSolution
        # make scaling and pivoting...
        scale = [max([abs(self.coList[i][j]) for j in range(n)]) for i in range(n)]                 #for coefficient matrix
        for i in range(n):                                                                          #
            pivot.pivot(self.coList, n, i, scale, self.equal)                                       #
        self.stepSolution += "Pivoted Coefficient Matrix:\n" + Print.writematrix(self.coList)       #
        self.stepSolution += "Pivoted Free Terms Vector:\n" + Print.writevector(self.equal)         #

        for i in range(n):
            if self.coList[i][i]==0:
                self.edyAlert("Cannot be solved by gauss seidel")
                return False,self.stepSolution
        print("Number of Iterations" + str(self.numOfIteration))
        for i in range(self.numOfIteration):                                                        #loop according to number of iteration
            print("Iteration Number:" + str(i))
            for j in range(len(self.equal)):                                                        #loop according to number of equations
                b = self.equal[j]                                                                   # store free term of row J in b
                for k in range(len(self.equal)):                                                    # loop in row of coefficient matrix
                    if k != j:                                                                                          ##  when k is not on main diagonal ,subtract ...
                        b = round(b - round(self.coList[j][k] * self.guess[k], self.precision), self.precision)         ## coefficient matrix of [j][k] * guess of [k] from b
                    else:                                                                                               ##otherwise continue
                        continue                                                                                        ##

                b = round(b / self.coList[j][j], self.precision)                                            # to get new element guess : divide b over element on main diagonal
                self.guess[j] = b                                                                           # add new element guess to guess list which will be returned
            self.stepSolution += "Iteration number:" + str(i+1) + "\n" + Print.writevector(self.guess)
        return self.guess, self.stepSolution

    def solveUsingrelative(self):
        relative = 1
        countdown=-1
        relativeError = [None] * len(self.equal)                                     # initialize new list of relative error
        n = len(self.coList)
        if det(self.coList) == 0:

            # Performs Gaussian Elimination to check whether it has an Infinite Solution or No Solution
            for i in range(0, n):
                for j in range(i + 1, n):
                    multiplier = round(self.coList[j][i] / (self.coList[i][i]), self.precision)
                    for k in range(i, n):
                        self.coList[j][k] = round(self.coList[j][k] + round(-multiplier * self.coList[i][k],
                                                                          self.precision),
                                                 self.precision)  # Use Multiplier to eliminate rows under pivot
                self.equal[j] = round(self.equal[j] + round(-multiplier * self.equal[i], self.precision))

            # Checks if a system has No solution
            for i in range(0, n):
                if self.coList[i][i] == 0 and self.equal[i] != 0:
                    self.stepSolution = "No Solution\n"
                    self.edyAlert("noSol")
                    return False, self.stepSolution

            # Else it has Infinite Solution
            self.stepSolution = "Infinite Solution\n"
            self.edyAlert("inf")
            return False,self.stepSolution
        scale = [max([abs(self.coList[i][j]) for j in range(n)]) for i in range(n)]             #
        for i in range(n):                                                                      # make scaling and pivoting...
            pivot.pivot(self.coList, n, i, scale, self.equal)                                   # for coefficient matrix
        self.stepSolution += "Pivoted Coefficient Matrix:\n" + Print.writematrix(self.coList)   #
        self.stepSolution += "Pivoted Free Terms Vector:\n" + Print.writevector(self.equal)     #
        no = 0
        check = self.testConverge(self.coList)                                           #
        if check == "may div":                                                           # use test convergence function and set countdown to 50
            countdown = 50                                                               # to stop infinate loop in case of diverge
            self.edyAlert("Result may diverge.")                                         #
        print(check)

        for i in range(n):
            if self.coList[i][i] == 0:
                self.edyAlert("Cannot be solved by gauss seidel")
                return False, self.stepSolution

        while relative > self.absoluteError and countdown != 0:                         # loop while relative error is not reached
            countdown = countdown - 1
            for j in range(len(self.equal)):                                            #loop according to number of equations
                b = self.equal[j]                                                       # store free term of row J in b
                for k in range(len(self.equal)):                                        # loop in row of coefficient matrix
                    if k != j:                                                                                             ##  when k is not on main diagonal ,subtract ...
                        b = round(b - round(self.coList[j][k] * self.guess[k], self.precision), self.precision)             ## coefficient matrix of [j][k] * guess of [k] from b
                    else:                                                                                                   ##otherwise continue
                        continue                                                                                            ##
                b = round(b / self.coList[j][j], self.precision)                                                            # to get new element guess : divide b over element on main diagonal
                if b == 0 and j == 0:
                    self.edyAlert("inf")
                    return False,steps
                else:
                    if b==0:
                        self.edyAlert("inf")
                        return False,steps
                    else:
                        relativeError[j] = abs((b - self.guess[j]) / b)
                # get relative error to check in while loop
                self.guess[j] = b                                                                 # add new element guess to guesslist

            no += 1
            self.stepSolution += "Iteration number:" + str(no) + "\n" + Print.writevector(self.guess)
            relative = max(relativeError)                                                              # get max relative error to determine continue loop or not
        return self.guess, self.stepSolution                                                        # guess list will be returned
#x+2y+3z=3
#-2z+y+9v=4
#3v+y=2
#y+3v=3

def det(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        val = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
        return val
    res = 0
    for curCol in range(len(matrix)):
        sign = (-1) ** (curCol)
        sub = det(getcf(matrix, 0, curCol))
        res += (sign * matrix[0][curCol] * sub)
    return res

# Complementary Function to Determinant Function
def getcf(m, i, j):
    return [row[: j] + row[j + 1:] for row in (m[: i] + m[i + 1:])]

if __name__ == "__main__":
    # a = [[1.0, 2.0, 3.0, 0.0], [0.0, 1.0, -2.0, 9.0], [0.0, 1.0, 0.0, 3.0], [0.0, 1.0, 0.0, 3.0]]
    # b = [3.0, 4.0, 2.0, 3.0]
    # a = [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]
    # b = [1.0, 2.0, 3.0]
    a = [[1,1],[1,1]]
    b = [0,3]
    obj = LinearInterface("Jacobi Iteration", 6, "isIteration", 10)
    inst = GaussSeidel(obj)
    inst.setGuess([0,1,1,0])
    solution,steps = inst.solve(a,b)
    print(steps)
    print(solution)
