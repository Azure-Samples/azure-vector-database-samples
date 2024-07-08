# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

from promptflow import tool


@tool
def calculate_hit_rate_at_k(
    retrieval_docs: list[dict], ground_truth_urls: str, k: list[int]
) -> dict:
    """Compute the hit rate based on ground truth. Hit Rate  = 1 if at least 1 document matches
    ground truth URL in the topK retrieved documents else 0. This is a more lose evaluation for
    precision as it ignores False Positives

    Args:
        retrieval_docs (list[dict]): the list of retrieved documents.
        ground_truth_urls (str): the '|' separated string of ground truth urls.
        k (list[int]): the k values for hit_rate@k

    Returns:
        dict: hit_rate@k for each value of k
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

    hit_rate_at_k = {}
    for _k in k:
        # Get the top k retrieved documents
        read_until = min([_k, len(retrieved_docs)])
        top_k_urls = retrieved_docs[:read_until]

        # Calculate the number of correctly predicted strings that are in the ground truth
        correct_predictions = len(set(top_k_urls) & set(ground_truth_urls))
        # Calculate the hit-rate@k
        hit_rate_at_k[_k] = 1 if correct_predictions > 0 else 0

    return hit_rate_at_k
