from LinearMethods import Jacobi,GaussJordan,GaussElim,Seidel,LUCLass

class LinearFactory:
    def use(self,obj):
        if obj.method == "Gauss Elimination":
            return GaussElim.GaussElimination(obj)
        elif obj.method == "Gauss Jordon":
            return GaussJordan.GaussJordon(obj)
        elif obj.method == "LU Decomposition":
            return LUCLass.LUDecomposition(obj)
        elif obj.method == "Gauss Siedel":
            return Seidel.GaussSeidel(obj)
        elif obj.method == "Jacobi Iteration":
            return Jacobi.JacobiIteration(obj)
