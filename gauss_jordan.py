# Gauss Jordan implementation

import numpy as np

def gauss_jordan(A, b):

    """
        Solves the linear system Ax = b using Gauss-Jordan elimination.
        Pre: A is a square matrix, b is a column vector
        Post: Returns the solution to the linear system Ax = b
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

def vector_sum(v1, v2):
    return [v1[i] + v2[i] for i in range(len(v1))]

def vector_sub(v1, v2):
    return [v1[i] - v2[i] for i in range(len(v1))]

def vector_scalar_mult(v, s):
    return [s * v[i] for i in range(len(v))]

def vector_dot(v1, v2):
    return sum([v1[i] * v2[i] for i in range(len(v1))])
