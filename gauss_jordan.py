# Gauss Jordan implementation

import numpy as np

def gauss_jordan(A, b):

    """Solves the linear system Ax = b using Gauss-Jordan elimination.
    """

    # Combine A and b into a single matrix
    Ab = np.hstack((A, b))

    # Perform Gauss-Jordan elimination
    for i in range(Ab.shape[0]):
        # Divide row i by the diagonal element
        Ab[i] /= Ab[i, i]
        # Subtract the row i from all other rows
        for j in range(Ab.shape[0]):
            if i != j:
                Ab[j] -= Ab[i] * Ab[j, i]

    # Extract the solution
    x = Ab[:, -1]

    return x

# gil el que lee

#pre:  .....