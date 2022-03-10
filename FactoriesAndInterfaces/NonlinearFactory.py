from NonlinearMethods import BisectionClass, NewtonRaphsonClass, SecantClass, RegulaFalsiClass, FixedPointClass


class NonlinearFactory:
    def use(self,obj):
        if obj.method == "Bisection":
            return BisectionClass.Bisection(obj)
        elif obj.method == "False-Position":
            return RegulaFalsiClass.RegulaFalsi(obj)
        elif obj.method == "Fixed-Point":
            return FixedPointClass.FixedPoint(obj)
        elif obj.method == "Newton Raphson":
            return NewtonRaphsonClass.NewtonRaphson(obj)
        elif obj.method == "Secant":
            return SecantClass.Secant(obj)
