# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

from promptflow import tool


@tool
def calculate_f1_at_k(prec: dict, rec: dict):
    """Compute the f1-score@k of the list of retrieved documents given a list
    ground truth url(s).
    This function, given the precisiojn@k and the recall@k, compute the f1-score@k
    .. math:: f1score = 2 \times \frac{\text{precision@k} \times \text{recall@k}}{\text{precision@k} + \text{recall@k}}
    f1-score is the harmonic mean of precision@k and recall@k

    Args:
        prec (dict): precision@k.
        rec (dict): recall@k.

    Returns:
        dict: F1 scores per K value
    """

    f1_at_k = {}
    mutual_k = set(prec.keys()) & set(rec.keys())

    for _k in mutual_k:
        # Calculate f1@k
        # Avoid division by zero in case there are no ground truth URLs

        f1_at_k[_k] = (
            2 * (prec[_k] * rec[_k]) / (prec[_k] + rec[_k])
            if (prec[_k] + rec[_k])
            else 0
        )

    return f1_at_k
