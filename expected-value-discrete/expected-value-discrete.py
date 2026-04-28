import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    x = np.asarray(x, dtype = float)
    p = np.asarray(p, dtype = float)
    
    if np.shape(p) != np.shape(x) or not np.isclose(np.sum(p), 1, atol = 1e-6):
        raise ValueError
    
    return float(np.sum(x * p))
