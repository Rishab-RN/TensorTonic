import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    x = np.asarray(x)
    mean = np.mean(x)
    median = np.median(x)
    
    freq = Counter(x)
    mf = max(freq.values())

    mode = float(min(k for k, v in freq.items() if v == mf))
    
    res = [mean, median, mode]
    return res   #return (mean, mode,)