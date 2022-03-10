
def writematrix(arr):
    """ Takes multidimensional list
            returns a Matrix Form as a string"""
    stepx = ""
    for row in arr:
        step = " ".join(map(str, row))
        stepx = stepx + step + "\n"
    return stepx + "\n\n"


def writevector(arr):
    """Takes List
            returns a Vector Form as a string"""
    step = '\n'.join(map(str, arr))
    return step + "\n\n"
