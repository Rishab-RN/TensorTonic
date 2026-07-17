import numpy as np

def f1_micro(y_true, y_pred) -> float:
    """
    Compute micro-averaged F1 for multi-class integer labels.
    """
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)

    if y_true.shape != y_pred.shape or len(y_true) == 0:
        return None

    tp = np.sum(y_true == y_pred)
    total = len(y_true)

    fp = total - tp
    fn = total - tp

    return float((2 * tp) / (2 * tp + fp + fn))