class LinearInterface:
    method = "Gauss Elimination"
    precision = 4
    method2 = None
    method2Value = None

    def __init__(self,m,p,m2=None,m2v=None,g=None):
        self.method = m
        self.precision = p
        self.is123 = True if m == "Gauss Elimination" or m == "Gauss Jordon" or m == "LU Decomposition" else False
        self.method2 = m2
        self.method2Value = m2v
