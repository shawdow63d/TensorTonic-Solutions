import numpy as np

def cross_entropy_loss(y_true, y_pred):
    sumn = 0.0
    for x in range(len(y_true)):
        sumn += np.log(y_pred[x][y_true[x]])
    return -1 / len(y_true) * sumn
    pass