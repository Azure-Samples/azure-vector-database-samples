# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

from promptflow import log_metric, tool


@tool
def calculate_rr(retrieval_docs: list[dict], ground_truth_urls: str):
    """Compute the RR of the list of retrieved documents given a list ground truth url(s).

    This function compute the Reciprocal Ranking (RR)
    .. math:: \text{mrr} = \frac{1}{\text{Rank of the First Correctly Retrieved Document}}
    The reciprocal rank of a query response is the multiplicative inverse of the rank of the first
    correct answer.

    Args:
        retrieval_docs (list[dict]): the list of retrieved documents.
        ground_truth_urls (str): Ground truth urls. '|' separates multiple correct values.

    Returns:
        float : Reciprocal Rank for each query
    """
    # if no documents are retrieved
    if len(retrieval_docs) == 0:
        return 0

    # if no ground truth is provided - empty string / None
    if not ground_truth_urls:
        return 0

    # split multiple valid answers to list. Convert urls to lower case.
    ground_truth_urls = ground_truth_urls.split("|")
    ground_truth_urls = [u.lower() for u in ground_truth_urls]

    # convert retrieved documents to lower case
    retrieval_urls = [d["source"].lower() for d in retrieval_docs]

    # if no matching documents are found
    if len(set(retrieval_urls) & set(ground_truth_urls)) == 0:
        return 0

    # calculate minimal rank
    for r, url in enumerate(retrieval_urls):
        if url in ground_truth_urls:
            break

    # compute rr
    rank = r + 1
    return 1 / rank
