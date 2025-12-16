import numpy as np

def mbe(y_true, y_pred):
    """Mean Absolute Error (MAE)"""
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    return np.mean(np.absolute(y_true - y_pred)) 