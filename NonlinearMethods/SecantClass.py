from math import log10

from PyQt5.QtWidgets import QMessageBox
from sympy import *
from sympy.abc import x,y

from FactoriesAndInterfaces.NonlinearInterface import NonlinearInterface
from NonlinearMethods.NewtonRaphsonClass import NewtonRaphson


def round_to_1(x, n):
    if x == 0 or n == 0:
        return x
    else:
     return round(x, -int(floor(log10(abs(x)))) + (n - 1))


# Implementing Secant Method
class Secant:


    def __init__(self, obj):
        self.method = obj.method
        self.figures = obj.precision
        self.N = obj.maxIterations
        self.e = obj.eps
        self.is125 = obj.is125

    def set2ndGuess(self,g2):
        self.x1 = g2

    def solve(self,expression, x0):
        x1 = self.x1
        print('\n\n*** SECANT METHOD IMPLEMENTATION ***')
        p1 = plot(expression, show=false)
        steps = ""
        step = 1
        condition = True
        while condition:
            if expression.subs(x, x0) == expression.subs(x, x1):
                steps += 'Divide by zero error!'
                self.edyAlert('Divide by zero error!')
                return False,steps


            p2 = plot(((x - x1) * (expression.subs(x, x0) - expression.subs(x, x1)) /
                       (x0 - x1)) + expression.subs(x, x1), show=false)
            p1.append(p2[0])

            x2 = round_to_1(x1 - round_to_1(x1 - x0, self.figures) * round_to_1(expression.subs(x, x1) /
                            round_to_1((expression.subs(x, x1) - expression.subs(x, x0)), self.figures), self.figures), self.figures)

            steps += "x0 = " + str(x0) + " and x1 = " + str(x1) + "\n"
            steps +=('Iteration-' + str(step) + ' x2 = ' + str(x2) + ' and f(x2) =' +
                     str(round_to_1(expression.subs(x, x2), self.figures)) + '\n')
            x0 = x1
            x1 = x2
            step = step + 1

            if step > self.N:
                steps += ('Not Convergent!')
                self.edyAlert("Divergent!")
                return False,steps

            condition = abs(round_to_1(expression.subs(x, x2), self.figures) )> self.e

        steps += ('\n Required root is: ' + str(round_to_1(x2, self.figures)))


        p1.save("Graphs of Nonlinear/Latest " + self.method + " Graph.png")
        return x2,steps

    def edyAlert(self, text="Error"):
        msg = QMessageBox()
        msg.setWindowTitle("Alert")
        msg.setText(text)
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()  # this will show our messagebox


if __name__ == "__main__":
    obj = NonlinearInterface("Newton Raphson",15,50,0.00001)
    inst = Secant(obj)
    inst.set2ndGuess(3)
    a,b = inst.solve(sympify("x^2-1"),2)
    print(b)