import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    A = np.asarray(A)
    n = A.shape[0]
    tr = 0

    for i in range(n):
        tr = tr + A[i][i]

    return tr
    pass
