def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    # Write code here
    def f(X):
        return 2*a*X + b
    for x in range (steps + 1):
        x0 = x0 - lr * f(x0)
    return x0
    pass