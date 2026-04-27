import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    a = np.asarray(a)
    b = np.asarray(b)
    x = np.sum(a*a)
    y = np.sum(b*b)
    if x == 0 or y == 0:
        return 0
    return float((np.sum(a*b))/(np.sqrt(x)*np.sqrt(y)))