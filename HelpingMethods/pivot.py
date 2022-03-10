def pivot(a, n, k, scale, b):
    """
        Pivots rows depending on their scaled pivots

        Parameters
        ----------
        param a: 2D array   # Our coeff matrix
        param n: int        # Number of equations
        param k: int        # Pivot index
        param scale: array  # Greatest value in each row
        param b: array      # Free variable array

        Variables
        ---------
        max : list, row with the maximum pivot
        max_row : float, index of the row with the maximum pivot
    """
    max = -1e50
    # Checks the row with the highest pivot
    for r in range(k, n):
        if max < abs(a[r][k] / scale[r]):
            max_row = r
            max = abs(a[r][k] / scale[r])

    # Swaps rows
    scale[k], scale[max_row] = scale[max_row], scale[k]
    a[k], a[max_row] = a[max_row], a[k]
    b[k], b[max_row] = b[max_row], b[k]
