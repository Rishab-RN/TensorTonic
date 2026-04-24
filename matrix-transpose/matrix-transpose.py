import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """

    A = np.asarray(A)
    n, m = A.shape
    
    y = np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            y[i][j] = A[j][i]
    return y
    pass
