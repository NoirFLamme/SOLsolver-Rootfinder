from HelpingMethods import Print
from PyQt5.QtWidgets import QMessageBox
from FactoriesAndInterfaces.LinearInterface import LinearInterface
import math,copy



class LUDecomposition:
    """
    Class for LU Decomposition with 3 different Decompositions
    """
    C = []  # -
    symmetric = True  # - Cholesky Decomposition Variables
    positiveDefinite = True  # -
    method2 = "dolittle"  # - Default Value
    precision = 4  # - Default Value
    stepSolution = ""  # Steps of solution in string
    numPivot = 0

    def __init__(self, obj):
        """
            @param obj:an object created by factory that implements methodInterface
            we use it to get our methods and precision

        """
        self.method = obj.method
        self.is123 = obj.is123
        self.precision = obj.precision
        self.method2 = obj.method2

    def pivot(self, array, free, isNotFirst=False):
        """
        Initializes values and pivots coefficient matrix and free term vector
        Checks if matrix is singular, and whether it has an Infinite Solution or No solution
        @param array : List of lists that contains our coefficients
        @param free :  List that contains our Free Terms
        @param isNotFirst Boolean that tells us if it's a First pivot or not. (Useful for Cholesky Decomposition)

        @return Boolean Which tells us if a matrix is Singular or Not.
        """

        self.n = len(array)
        self.array = array
        self.free = free

        if not isNotFirst:
            self.C = copy.deepcopy(self.array)  # Create a copy of our coefficient Matrix before Pivoting

        # Check if matrix is singular
        if det(self.array) == 0:

            # Performs Gaussian Elimination to check whether it has an Infinite Solution or No Solution
            for i in range(0, self.n):
                for j in range(i + 1, self.n):
                    multiplier = round(self.array[j][i] / (self.array[i][i]), self.precision)
                    for k in range(i, self.n):
                        self.array[j][k] = round(self.array[j][k] + round(-multiplier * self.array[i][k],
                                                                          self.precision),
                                                 self.precision)  # Use Multiplier to eliminate rows under pivot
                self.free[j] = round(self.free[j] + round(-multiplier * self.free[i], self.precision))

            # Checks if a system has No solution
            for i in range(0, self.n):
                if self.array[i][i] == 0 and self.free[i] != 0:
                    self.stepSolution = "No Solution\n"
                    self.edyAlert("noSol")
                    return False

            # Else it has Infinite Solution
            self.stepSolution = "Infinite Solution\n"
            self.edyAlert("inf")
            return False

        # Loops through diagonal elements, finds biggest absolute number
        # Replaces Rows in coefficient Matrix and Free Terms Vector

        self.numPivot += 1
        for i in range(0, self.n):

            max_number = abs(self.array[i][i])
            max_row = i
            for k in range(i + 1, self.n):
                if abs(self.array[k][i]) > max_number:
                    max_number = abs(self.array[k][i])
                    max_row = k

            self.array[i], self.array[max_row] = self.array[max_row], self.array[i]
            self.free[i], self.free[max_row] = self.free[max_row], self.free[i]

        if self.numPivot == 1:

            self.stepSolution += "Pivoted Matrix: \n"
            self.stepSolution += Print.writematrix(self.array)
            self.stepSolution += "Pivoted Free Terms:" + "\n"
            self.stepSolution += Print.writevector(self.free)
            return True
        else:
            return True

    def solve(self, array, free):
        """
        @param array : List of lists that contains our coefficients
        @param free :  List that contains our Free Terms

        @return Solution Vector or returns False if Validation checks fail
         """

        # Checks Singularity and Pivots Matrix and Free Terms
        isValid = self.pivot(array, free)
        if not isValid:
            return False, self.stepSolution

        # Doolittle Decomposition
        if self.method2 == "dolittle":

            # Set diagonal elements in L to 1 and the rest 0
            L = [[0 for i in range(self.n)] for i in range(self.n)]
            for i in range(0, self.n):
                L[i][i] = 1

            # Copy Coefficient Matrix to U
            U = self.array

            # Perform Gaussian Elimination to U
            for i in range(0, self.n):
                for j in range(i + 1, self.n):
                    multiplier = round(U[j][i] / (U[i][i]), self.precision)
                    L[j][i] = multiplier  # Get Multiplier and put it in L Matrix
                    for k in range(i, self.n):
                        U[j][k] = round(U[j][k] + round(-multiplier * U[i][k], self.precision),
                                        self.precision)  # Use Multiplier to eliminate rows under pivot
                self.pivot(U, self.free, True)  # Pivot after each Columnwise Elimination

            self.stepSolution += "Lower Triangular Matrix: \n"
            self.stepSolution += Print.writematrix(L)
            self.stepSolution += "Upper Triangular Matrix: \n"
            self.stepSolution += Print.writematrix(U)

        # Crout Decomposition
        elif self.method2 == "crout":

            U = [[0 for i in range(self.n)] for i in range(self.n)]
            L = [[0 for i in range(self.n)] for i in range(self.n)]

            for j in range(0, self.n):  # Loops through each column
                U[j][j] = 1  # Set diagonal elements in U to 1

                for i in range(j, self.n):  # Loops through each row beginning from diagonal elements
                    sum = 0
                    for k in range(0, j):
                        sum = round(sum + round(L[i][k] * U[k][j], self.precision),
                                    self.precision)  # Calculate sum by Crout's Algorithm (Matrix Multiplication)
                    L[i][j] = round(self.array[i][j] - sum, self.precision)  # Use sum to get L elements

                for i in range(j, self.n):  # Loops through each row beginning from diagonal elements
                    sum = 0
                    for k in range(0, j):
                        sum = round(sum + round(L[j][k] * U[k][i], self.precision),
                                    self.precision)  # Calculate sum by Crout's Algorithm (Matrix Multiplication)
                    U[j][i] = round(round((self.array[j][i] - sum), self.precision) / L[j][j],
                                    self.precision)  # Use sum to get U elements

            self.stepSolution += "Lower Triangular Matrix: \n"
            self.stepSolution += Print.writematrix(L)
            self.stepSolution += "Upper Triangular Matrix: \n"
            self.stepSolution += Print.writematrix(U)

        # Cholesky Decomposition
        elif self.method2 == "cholesky":

            CH = copy.deepcopy(self.C)  # Make a copy of our C Matrix
            self.stepSolution += "No pivot Matrix: \n"
            self.stepSolution += Print.writematrix(CH)

            # Checks if Matrix C is symmetric or not
            for i in range(0, self.n):
                for j in range(0, self.n):
                    if self.C[i][j] != self.C[j][i]:
                        self.symmetric = False
            self.stepSolution += "Is matrix Symmetric: " + str(self.symmetric) + "\n\n"

            # Uses Gaussian Elimination to Check our pivots
            for i in range(0, self.n):
                for j in range(i + 1, self.n):
                    m = round(self.C[j][i] / (self.C[i][i]), self.precision)
                    for k in range(i, self.n):
                        self.C[j][k] = round(self.C[j][k] + round(-m * self.C[i][k], self.precision),
                                             self.precision)
            self.stepSolution += "Row Echelon Form Matrix: \n"
            self.stepSolution += Print.writematrix(self.C)

            # Checks if Matrix C is Positive Definite or not
            for i in range(0, self.n):  # Loops through our diagonal Elements ( pivots)
                if self.C[i][i] <= 0:  # Checks if all of them are positive or not.
                    self.positiveDefinite = False
            self.stepSolution += "Is matrix Positive Definite: " + str(self.positiveDefinite) + "\n\n"

            # Error Handling (if a user wanted to do a Cholesky Decomposition on a non-Symmetric or a non-Positive Definite Matrix)
            if not self.symmetric or not self.positiveDefinite:
                self.stepSolution += "This matrix is not Symmetric or not Positive Definite, please enter a valid Matrix to perform Cholesky Decomposition\n"
                self.edyAlert(
                    "This matrix is not Symmetric or not Positive Definite, please enter a valid Matrix to perform Cholesky Decomposition")
                return False,self.stepSolution

            L = [[0 for i in range(self.n)] for i in range(self.n)]
            U = [[0 for i in range(self.n)] for i in range(self.n)]

            for j in range(0, self.n):  # Loops through each column
                for i in range(j, self.n):  # Loops through each row beginning from diagonal elements
                    if i == j:  # Algorithm for diagonal elements
                        sum = 0
                        for k in range(0, j):
                            sum = round(sum + round(L[i][k] ** 2, self.precision), self.precision)
                        L[i][j] = round(math.sqrt(round((CH[i][j] - sum), self.precision)), self.precision)
                    else:  # Algorithm for non-diagonal elements
                        sum = 0
                        for k in range(0, j):
                            sum = round(sum + round(L[i][k] * L[j][k], self.precision), self.precision)
                        L[i][j] = round(round((CH[i][j] - sum), self.precision) / L[j][j], self.precision)

            self.stepSolution += "Lower Triangular Matrix: \n"
            self.stepSolution += Print.writematrix(L)

            # Find Transpose of L and assign it to U
            for i in range(0, self.n):
                for j in range(0, self.n):
                    U[i][j] = L[j][i]

            self.stepSolution += "Upper Triangular Matrix: \n"
            self.stepSolution += Print.writematrix(U)

        else:  # If another nonLinearMethod was entered Return
            return

        # Forward Substitution Algorithm
        Y = [0 for i in range(self.n)]
        for i in range(0, self.n):
            sum = self.free[i]
            for k in range(0, i):
                sum = round(sum - round(Y[k] * L[i][k], self.precision), self.precision)
            Y[i] = round(sum / L[i][i], self.precision)

        self.stepSolution += "LY Vector (Forward Substitution): \n"
        self.stepSolution += Print.writevector(Y)

        # Backward Substitution Algorithm
        X = [0 for i in range(self.n)]
        X[self.n - 1] = round(Y[self.n - 1] / U[self.n - 1][self.n - 1], self.precision)
        for i in range(self.n - 2, -1, -1):
            sum = 0
            for j in range(i + 1, self.n):
                sum = round(sum + round(U[i][j] * X[j], self.precision), self.precision)
                X[i] = round(round((Y[i] - sum), self.precision) / U[i][i], self.precision)

        # zero very small elements
        tol = 0.5 * 10 ** (2 - self.precision)
        for i in range(len(X)):
            if abs(X[i]) < tol:
                X[i] = 0.0

        self.stepSolution += "UX Vector (solution) (Backward Substitution): \n"
        self.stepSolution += Print.writevector(X)
        return X,self.stepSolution

    # Method that displays alert in GUI
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

# Complementary Function to Determinant Function
def getcf(m, i, j):
    return [row[: j] + row[j + 1:] for row in (m[: i] + m[i + 1:])]

# Determinant Function
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



