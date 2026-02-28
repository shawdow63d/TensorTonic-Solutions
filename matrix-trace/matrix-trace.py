import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    # Write code here
    sz = np.shape(A)
    sumx = 0
    for i in range(sz[0]):
        sumx += A[i][i]
    return sumx
    pass
