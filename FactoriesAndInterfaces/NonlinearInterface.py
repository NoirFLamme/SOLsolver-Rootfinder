class NonlinearInterface:
    method = "Gauss Elimination"
    precision = 4
    maxIterations = 50
    eps = 0.0001

    def __init__(self,m,p,mi,e):
        self.method = m
        self.precision = p
        self.is125 = True if m == "Bisection" or m == "False-Position" or m == "Secant" else False
        self.maxIterations = mi
        self.eps = e



#secant 2 pts
#newton,fixed 1 pt
#bisec,faalse [,]