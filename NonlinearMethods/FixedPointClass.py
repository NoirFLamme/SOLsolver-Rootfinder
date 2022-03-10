import math

from PyQt5.QtWidgets import QMessageBox
from sympy import *
from sympy.abc import x
import matplotlib.pyplot as plt
import numpy as np

from FactoriesAndInterfaces.NonlinearInterface import NonlinearInterface
def round_to_1(x, n):
    if x == 0 or n == 0:
        return x
    else:
        return round(x, -int(math.floor(math.log10(abs(x)))) + (n - 1))

class FixedPoint:
    stepsolution = ""
    def __init__(self, obj):
        self.method = obj.method
        self.tol = obj.eps
        self.maxiteration = obj.maxIterations
        self.precision = obj.precision
        self.is125 = obj.is125

    #iter     : number of iteration
    # tol     : abs relative error
    # self.x0 : initial guess point
    def solve(self,exp,x0):
        self.exp = exp
        self.x0 = x0
        const=-1
        for i in range(200):
            g = x + const * self.exp
            D=diff(g, x)
            test = round_to_1(D.subs(x, self.x0).evalf(), self.precision)
            if abs(test) < 1:
                self.stepsolution += "Solution converges\n\n\n"
                break
            const=const+0.01
        if const >= 1:
            self.stepsolution += "Diverges"
            self.edyAlert("Divergent!\n")
            return False,self.stepsolution
        g = x+const*self.exp                           # f=exp  , exp = f = 0  , x = g   ---->  g - x = 0  ,, g = f + x
        iter = 0
        tol = 1
        LimX=[]
        LimY=[]
        while iter < self.maxiteration and tol > self.tol:                  # go on when not reach max iteration and error greater than tolerance
            x1 = round_to_1(g.subs(x, self.x0).evalf(), self.precision)     # calculate xi
            self.stepsolution += "step "+ str(iter+1) + "\n"
            self.stepsolution += "Xi= " +  str(x1) + "\n"
            LimX.append(self.x0)
            LimY.append(x1)
            if x1 != 0:
                tol = abs((x1 - self.x0) / x1 )                                      # tol = (new-old) /new
                self.stepsolution += "relative error : " +  str(tol) + "\n\n\n"
            self.x0 = x1                                                    # reasign x0
            iter = iter + 1                                 # increase iteration
        # plotting graph
        p2 = plot(x, show=false)
        p1 = plot(g, show=false, xlim=[-min(LimX)*1.2, max(LimX)*1.2], ylim=[-min(LimY)*1.2, max(LimY)*1.2])
        p1.append(p2[0])
        p1.show()
        # p1.save("Graphs of Nonlinear/Latest " + self.method + " Graph.png")
        self.stepsolution += "Solution is " + str(x1)
        return x1,self.stepsolution

    def edyAlert(self, text="Error"):
        msg = QMessageBox()
        msg.setWindowTitle("Alert")
        msg.setText(text)
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()  # this will show our messagebox


if __name__ == "__main__":
    obj = NonlinearInterface("Newton Raphson",15,50,0.00001)
    inst = FixedPoint(obj)
    a,b = inst.solve(sympify("x-sin(x)-0.5"),2)
    print(b)










