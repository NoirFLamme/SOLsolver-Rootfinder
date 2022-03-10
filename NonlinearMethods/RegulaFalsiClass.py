
import math
from PyQt5.QtWidgets import QMessageBox
from sympy import *
from numpy import *
from matplotlib import *
import matplotlib.pyplot as plt

x = symbols("x")


class RegulaFalsi:
    expression = ""
    precision = 10
    EPS = 0.00001
    maxIterations = 50
    stepSolution = ""
    lower = 0
    upper = 1

    def __init__(self, obj):
        """

        :param obj: Non-Linear factory object.
        """
        self.method = obj.method
        self.precision = obj.precision
        self.maxIterations = obj.maxIterations
        self.EPS = obj.eps
        self.is125 = obj.is125

    def validate(self):
        """
        Method that validates the interval of the equation.

        :returns: boolean
        """
        if self.fl * self.fu < 0:
            return True
        else:
            return False

    def plot(self):
        """
        Method that initializes the graph of our function.

        """
        fx = lambdify(x, self.expression, modules=['numpy'])
        xVals = linspace(self.lower - 10, self.upper + 10)
        plt.plot(xVals, fx(xVals))
        plt.axis([self.lower - 10, self.upper + 10, -10, 10])
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.plot([0, 0], [-10, 10])
        plt.plot([self.lower - 10, self.upper + 10], [0, 0])
        plt.plot([self.lower, self.upper], [self.fl, self.fu], color="red")

    def set2ndGuess(self, u):
        """
        Method that gets the upper bound.

        :param u: Upper Bound
        """
        self.upper = u

    def solve(self, exp, l):
        """
        Method that solves for root of equation.

        :param exp: String Expression
        :param l: Lower Bound
        :return: root(Float)  Step Solution (String)
        """

        self.expression = exp
        self.lower = l
        self.fl = self.expression.subs(x, self.lower).evalf()
        self.fu = self.expression.subs(x, self.upper).evalf()

        self.plot()

        if not self.validate():
            self.stepSolution = "Function has same sign at end points, Please enter a valid Interval."
            self.stepSolution = "Function has same sign at end points, Please enter a valid Interval."
            self.edyAlert(self.stepSolution)
            return False, self.stepSolution

        i = 0
        root = 0
        while i < self.maxIterations:
            self.stepSolution += "\n" + "   Iteration:" + str(i + 1)
            f1 = root
            root = round_to_1(self.lower - round_to_1((round_to_1((self.upper - self.lower), self.precision) * self.fl / round_to_1(
                (self.fu - self.fl), self.precision)), self.precision), self.precision)
            self.stepSolution += "\n" + "New Root: " + str(root)
            fr = round_to_1(self.expression.subs(x, root).evalf(), self.precision)
            self.stepSolution += "\n" + "New F(root): " + str(fr)
            f2 = root
            error = abs(f2 - f1)
            self.stepSolution += "\n" + "New error: " + str(error) + " > " + str(self.EPS) + "\n"
            if error < self.EPS:
                break
            if fr == 0:
                self.stepSolution += "\n\n" + "Root is: " + str(root)
                return root
            elif round_to_1(self.fl * fr, self.precision) < 0:
                self.upper = root
                self.fu = round_to_1(self.expression.subs(x, self.upper).evalf(), self.precision)
            else:
                self.lower = root
                self.fl = round_to_1(self.expression.subs(x, self.lower).evalf(), self.precision)
            i += 1
            plt.plot([self.lower, self.upper], [self.fl, self.fu], color="red")
        self.stepSolution += "\n\n" + "Root is: " + str(root)
        plt.savefig("Graphs of Nonlinear/Latest " + self.method + " Graph.png")
        plt.show()
        return root, self.stepSolution

    def edyAlert(self, text="Error"):
        msg = QMessageBox()
        msg.setWindowTitle("Alert")
        msg.setText(text)
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()  # this will show our messagebox

def round_to_1(x, n):
    if x == 0 or n == 0:
        return x
    else:
        return round(x, -int(math.floor(math.log10(abs(x)))) + (n - 1))