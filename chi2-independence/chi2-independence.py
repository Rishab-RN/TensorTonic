import numpy as np

def chi2_independence(C):
    """
    Compute chi-square test statistic and expected frequencies.
    """
    c = np.asarray(C)

    rsum = np.sum(c, axis = 1, keepdims = True)
    csum = np.sum(c, axis = 0, keepdims = True)
    total = np.sum(c)

    expected = (rsum * csum) / total
    chi = np.sum(((c - expected) ** 2) / expected)

    return float(chi), expected