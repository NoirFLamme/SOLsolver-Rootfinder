from HelpingMethods import Print,pivot
from PyQt5.QtWidgets import QMessageBox
from FactoriesAndInterfaces.LinearInterface import LinearInterface

class GaussJordon:
    precision = 4
    def __init__(self, obj):
        self.method = obj.method
        self.precision = obj.precision
        self.is123 = obj.is123

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

    def solve(self,a, b):
        """
           Evaluates the solution of a system of linear equations using Gauss Jordan nonLinearMethod

           Parameters
           ----------
           param array: 2D array
           param free: array

           Variables
           ---------
           tol: float, used for singularity check to avoid division by 0
           n: int, length of the coeff array (a)
           scale: list, list of the maximum scales in each row (used in pivoting)

           Returns
           -------
           steps: string, records the steps of the solution
           sol: list, initial solution array
        """

        # Defines tolerance for singularity check
        steps = ""
        tol = 0.000000000000000000001
        n = len(a)

        sol = [0] * (n)

        # Extracts the maximum values out of each row for scaling
        scale = [max([abs(a[i][j]) for j in range(n)]) for i in range(n)]

        # Forward Elimination
        """ 
           Pivots every row, and commits gauss elimination using iterations
           Checks for singularity in each iteration
        """
        steps += "Forward Elimination: \n"
        for k in range(0, n - 1):
            # Pivoting and scaling
            pivot.pivot(a, n - 1, k, scale, b)
            # Printing pivoting steps
            steps += "After pivoting row " + str(k + 1) + "\n"
            steps += Print.writematrix(a)

            #Check for singularity
            if abs(a[k][k]/scale[k]) < tol:
                self.edyAlert("inf")
                return False,steps

            for i in range(k + 1, n):
                factor = round(a[i][k] / a[k][k], self.precision)
                for j in range(k + 1, n):
                    a[i][j] = round(a[i][j] - round((factor * a[k][j]), self.precision), self.precision)
                b[i] = round(b[i] - round((factor * b[k]), self.precision), self.precision)

        steps += "After pivoting row " + str(n) + "\n"
        steps += Print.writematrix(a)

        for k in range(1, n):
            for i in range(0, k):
                a[k][i] = 0
        # Printing result after Forward elimination
        steps += "Removing the lower triangle \n"
        steps += Print.writematrix(a)

        if abs(a[n - 1][n - 1]) < tol:
                if abs(b[n-1]) < tol:
                    self.edyAlert("inf")
                else:
                    self.edyAlert("noSol")
                return False,steps

        # Backward elimination
        """ 
              Proceed to commit backward elimination, and added redundant steps just for extra measures
              Checks for singularity in each iteration
        """
        steps += "Backward Elimination:\n"
        for k in range(n - 1, 0, -1):

            # Printing matrix after each iteration
            steps += "Row " + str(k + 1) + "\n"
            steps += Print.writematrix(a)

            if abs(a[k][k]) < tol:
                self.edyAlert(
                    "Your equations have infinite number of solution. Thus, cannot be solved. Please re-enter.")
                return False,steps

            for i in range(k - 1, -1, -1):
                factor = a[i][k] / a[k][k]
                for j in range(k - 1, -1, -1):
                    a[i][j] = round(a[i][j] - round((factor * a[k][j]), self.precision), self.precision)
                b[i] = round(b[i] - round((factor * b[k]), self.precision), self.precision)
        # Printing matrix after each iteration
        steps += "Row " + str(1) + "\n"
        steps += Print.writematrix(a)

        for k in range(1, n):
            for i in range(0, k):
                a[i][k] = 0

        # Printing result after Backward elimination
        steps += "Removing the upper  \n"
        steps += Print.writematrix(a)

        # Check for singularity
        if abs(a[n - 1][n - 1]) < tol:
            self.edyAlert("inf")
            return False, steps

        # Backward Substitution
        """ 
          Commits backward substitution by looping over the matrix, and subtracting and diving
          in each step to evaluate the solution for each variable
        """
        sol[n - 1] = b[n - 1] / a[n - 1][n - 1]
        for k in range(n - 2, -1, -1):
            sum = 0
            for j in range(k + 1, n):
                sum = round(sum + round(a[k][j] * sol[j], self.precision), self.precision)
            if abs(a[k][k]) < tol:
                self.edyAlert("inf")
                return False,steps
            sol[k] = round((b[k] - sum) / a[k][k], self.precision)

        for i in range(len(sol)):
            if abs(sol[i]) < tol:
                sol[i] = 0.0

        steps += "Solution:\n"
        steps += Print.writevector(sol)
        return sol,steps


