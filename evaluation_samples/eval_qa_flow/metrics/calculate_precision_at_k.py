# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

from promptflow import tool


@tool
def calculate_precision_at_k(
    retrieval_docs: list[dict], ground_truth_urls: str, k: list[int]
) -> dict:
    """Compute the precision@k of the list of retrieved documents given a list
    ground truth url(s).

    This function compute the precision@k
    .. math:: \text{precision@k} = \frac{\text{number of relevant documents in top k}}{k}
    precision@K counts how many ground truth url(s) are included in the retrieved k links.

    Args:
        retrieval_docs (list[dict]): the list of retrieved documents.
        ground_truth_urls (str): the '|' separated string of ground truth urls.
        k (list[int]): the k values for precision@k

    Returns:
        dict: precision@k for each value of k
    """
    # no ground truth provided
    if not ground_truth_urls:
        return {}

    ground_truth_urls = ground_truth_urls.split("|")
    ground_truth_urls = [u.lower() for u in ground_truth_urls]

    # no ground truth provided
    if len(ground_truth_urls) == 0:
        return {}

    # no retrieved documents
    if len(retrieval_docs) == 0:
        return {}

    # extract urls from retrieved documents
    retrieved_docs = [d["source"].lower() for d in retrieval_docs]

    precision_at_k = {}
    for _k in k:
        # Get the top k retrieved documents
        read_until = min([_k, len(retrieved_docs)])
        top_k_urls = retrieved_docs[:read_until]

        # Calculate the number of correctly predicted strings that are in the ground truth
        correct_predictions = len([i for i in top_k_urls if i in ground_truth_urls])
        # Calculate the precision@k
        precision_at_k[_k] = correct_predictions / read_until

    return precision_at_k
