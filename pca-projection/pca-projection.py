import numpy as np

def pca_projection(X, k):
    """
    Project data onto the top-k principal components.
    """
    # Write code here
    X = np.array(X)
    X_centered = X - X.mean(axis = 0)
    U, s, Vt = np.linalg.svd(X_centered)
    W2 = Vt[ : k].T
    X2D = X_centered @ W2
    return X2D