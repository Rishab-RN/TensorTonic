import numpy as np

def t_test_one_sample(x, mu0):
    """
    Compute one-sample t-statistic.
    """
    mean = np.mean(x)
    s = np.sqrt((np.sum((x - mean) ** 2)) / (len(x) - 1))
    return (mean - mu0) * np.sqrt(len(x)) / s