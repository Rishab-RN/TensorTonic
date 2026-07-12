import numpy as np

def matrix_normalization(matrix, axis=None, norm_type='l2'):
    """
    Normalize a 2D matrix along specified axis using specified norm.
    """
    try:
        matrix = np.asarray(matrix, dtype=float)

        # Check if input is 2D
        if matrix.ndim != 2:
            return None

        # Compute the norm
        if norm_type == 'l1':
            norm = np.sum(np.abs(matrix), axis=axis, keepdims=True)
        elif norm_type == 'l2':
            norm = np.sqrt(np.sum(matrix ** 2, axis=axis, keepdims=True))
        elif norm_type == 'max':
            norm = np.max(np.abs(matrix), axis=axis, keepdims=True)
        else:
            return None

        # Avoid division by zero
        norm[norm == 0] = 1

        return matrix / norm

    except:
        return None
    