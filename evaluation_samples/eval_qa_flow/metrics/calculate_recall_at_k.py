# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

from promptflow import tool


@tool
def calculate_recall_at_k(
    retrieval_docs: list[dict], ground_truth_urls: str, k: list[int]
) -> dict:
    """Compute the recall@k of the list of retrieved documents given a list
    ground truth url(s).

    This function compute the recall@k
    .. math:: \text{precision@k} = \frac{\text{ # relevant documents in top k}}{# ground truth urls}
    recall@K counts how many ground truth url(s) are retrieved in the top-k retrieved documents

    Args:
        retrieval_docs (list[dict]): the list of retrieved documents.
        ground_truth_urls (str): the '|' separated string of ground truth urls.
        k (list[int]): the k values for precision@k

    Returns:
        dict: recall@k for each value of k
    """
    # no ground truth provided
    if not ground_truth_urls:
        return {}

    ground_truth_urls = ground_truth_urls.split("|")
    ground_truth_urls = [u.lower() for u in ground_truth_urls]

    # extract urls from retrieved documents
    retrieved_docs = [d["source"].lower() for d in retrieval_docs]

    recall_at_k = {}
    for _k in k:
        # Get the top k retrieved documents
        read_until = min([_k, len(retrieved_docs)])
        top_k_urls = retrieved_docs[:read_until]

        # Calculate the number of correctly predicted strings that are in the ground truth
        correct_predictions = len(set(top_k_urls) & set(ground_truth_urls))

        # Calculate the precision@k
        recall_at_k[_k] = correct_predictions / len(ground_truth_urls)

    return recall_at_k
