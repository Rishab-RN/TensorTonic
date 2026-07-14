import numpy as np

def calculate_eigenvalues(matrix):
    """
    Calculate eigenvalues of a square matrix.
    """
    try:
        matrix = np.asarray(matrix, dtype=float)

        # Check for valid square matrix
        if matrix.ndim != 2:
            return None

        rows, cols = matrix.shape
        if rows == 0 or rows != cols:
            return None

        # Compute eigenvalues
        eigenvalues = np.linalg.eigvals(matrix)

        # Sort by real part, then imaginary part
        idx = np.lexsort((eigenvalues.imag, eigenvalues.real))

        return eigenvalues[idx]

    except:
        return None