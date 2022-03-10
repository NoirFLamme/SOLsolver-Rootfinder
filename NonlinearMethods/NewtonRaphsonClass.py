from math import log10

from PyQt5.QtWidgets import QMessageBox
from sympy import *

from sympy.abc import x,y

from FactoriesAndInterfaces.NonlinearInterface import NonlinearInterface


def round_to_1(x, n):
    if x == 0 or n == 0:
        return x
    else:
     return round(x, -int(floor(log10(abs(x)))) + (n - 1))


# Implementing Newton Raphson Method
class NewtonRaphson:

    def __init__(self, obj):
        self.method = obj.method
        self.figures = obj.precision
        self.N = obj.maxIterations
        self.e = obj.eps
        self.is125 = obj.is125


    def solve(self, expression, x0):
        print('\n\n*** NEWTON RAPHSON METHOD IMPLEMENTATION ***')
        p1 = plot(expression, show=false)
        steps = ""
        step = 1
        flag = 1
        condition = True
        while condition:
            derivative = diff(expression, x)
            if round_to_1(derivative.subs(x , x0), self.figures) == 0.0:
                steps += 'Divide by zero error!'
                self.edyAlert('Divide by zero error!')
                return False,steps

            p2 = plot((x - x0) * derivative.subs(x , x0) + expression.subs(x, x0), show = false)
            p1.append(p2[0])
            x1 = round_to_1(x0 - round_to_1(expression.subs(x, x0) / derivative.subs(x , x0), self.figures), self.figures)
            steps += ('Iteration-' + str(step) + ' x1 = ' + str(x1) + ' and f(x2) =' +
                      str(round_to_1(expression.subs(x, x1), self.figures)) + '\n')
            x0 = x1
            step = step + 1

            if step > self.N:
                flag = 0
                break

            condition = abs(round_to_1(expression.subs(x, x1), self.figures)) > self.e

        if flag == 1:
            steps += ('\n Required root is: ' + str(round_to_1(x1, self.figures)))
        else:
            steps += '\nNot Convergent.'
            self.edyAlert('Divergent!')
            return False,steps

        p1.save("Graphs of Nonlinear/Latest " + self.method + " Graph.png")
        return x1,steps

    def edyAlert(self, text="Error"):
        msg = QMessageBox()
        msg.setWindowTitle("Alert")
        msg.setText(text)
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()  # this will show our messagebox

if __name__ == "__main__":
    obj = NonlinearInterface("Newton Raphson",15,50,0.00001)
    inst = NewtonRaphson(obj)
    a,b = inst.solve(sympify("x^2-1"),2)
    print(b)


