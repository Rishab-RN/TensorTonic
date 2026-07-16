import numpy as np

def classification_metrics(y_true, y_pred, average="micro", pos_label=1):
    """
    Compute accuracy, precision, recall, F1 for single-label classification.
    Averages: 'micro' | 'macro' | 'weighted' | 'binary' (uses pos_label).
    Return dict with float values.
    """
    try:
        y_true = np.asarray(y_true)
        y_pred = np.asarray(y_pred)

        if y_true.shape != y_pred.shape:
            return None

        n = len(y_true)
        if n == 0:
            return None

        accuracy = np.mean(y_true == y_pred)

        labels = np.unique(np.concatenate((y_true, y_pred)))
        k = len(labels)

        label_to_idx = {label: i for i, label in enumerate(labels)}

        cm = np.zeros((k, k), dtype=int)

        for t, p in zip(y_true, y_pred):
            cm[label_to_idx[t], label_to_idx[p]] += 1

        TP = np.diag(cm)
        FP = np.sum(cm, axis=0) - TP
        FN = np.sum(cm, axis=1) - TP
        support = np.sum(cm, axis=1)

        def safe_div(a, b):
            return np.divide(a, b, out=np.zeros_like(a, dtype=float), where=b != 0)

        precision = safe_div(TP, TP + FP)
        recall = safe_div(TP, TP + FN)
        f1 = safe_div(2 * precision * recall, precision + recall)

        if average == "micro":
            tp = TP.sum()
            fp = FP.sum()
            fn = FN.sum()

            p = tp / (tp + fp) if tp + fp else 0
            r = tp / (tp + fn) if tp + fn else 0
            f = 2 * p * r / (p + r) if p + r else 0

        elif average == "macro":
            p = precision.mean()
            r = recall.mean()
            f = f1.mean()

        elif average == "weighted":
            weights = support / support.sum()
            p = np.sum(precision * weights)
            r = np.sum(recall * weights)
            f = np.sum(f1 * weights)

        elif average == "binary":
            if pos_label not in label_to_idx:
                return None

            idx = label_to_idx[pos_label]
            p = precision[idx]
            r = recall[idx]
            f = f1[idx]

        else:
            return None

        return {
            "accuracy": float(accuracy),
            "precision": float(p),
            "recall": float(r),
            "f1": float(f)
        }

    except:
        return None