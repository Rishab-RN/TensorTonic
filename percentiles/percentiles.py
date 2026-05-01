import numpy as np

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    
    x = np.asarray(x, dtype = float)
    q = np.asarray(q, dtype = float)

    return np.percentile(x, q, method = 'linear')
    
    # x = np.sort(np.asarray(x))
    # q = np.asarray(q)

    # n = len(x)
    # pos = q / 100 * (n - 1)

    # lower = np.floor(pos).astype(int)
    # upper = np.ceil(pos).astype(int)

    # res = x[lower] + (pos - lower) * (x[upper] - x[lower])

    # return res