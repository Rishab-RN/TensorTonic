import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    y = np.asarray(y)

    if len(y) == 0:
        return 0.0

    _, count = np.unique(y, return_counts = True)

    p = count/count.sum()
    p = p[p > 0]

    return float(-np.sum(p * np.log2(p)))