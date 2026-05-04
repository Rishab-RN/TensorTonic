import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    v = np.asarray(v)
    return np.diag(v)


    # Vectorized approach
    # v = np.asarray(v)
    # n = len(v)
    # res = np.zeros((n, n))
    # res[np.arange(n), np.arange(n)] = v
    # return res


    # Using loop
    # v = np.asarray(v)
    # n = len(v)
    # res = np.zeros((n, n))
    
    # for i in range(n):
    #     res[i][i] = v[i]
    
    # return res