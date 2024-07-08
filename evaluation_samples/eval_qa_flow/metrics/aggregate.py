# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

from typing import List

from promptflow import log_metric, tool


@tool
def aggregate(
    prec_res: List[dict],
    rec_res: List[dict],
    f1_res: List[dict],
    mrr_res: List[float],
    hit_rate_res: List[dict],
):
    """
    This tool aggregates the precision@k, recall@k, f1-score@k, mrr and hit_rate_res@K,
    of all lines and calculate the average metric. The code logs the metrics for comparison

    :param prec_res,rec_res,f1_res: List of the output of the precision@k, recall@k,
    f1-score@k node, respectively.
    :param mrr: List of the output of mrr@k node
    """

    results = {
        "precision": prec_res,
        "recall": rec_res,
        "f1": f1_res,
        "hit_rate": hit_rate_res,
    }

    for metric, processed_results in results.items():
        # extract all K values which were calculated for the metric
        metric_valid_k = processed_results[0].keys()

        aggregated_result = {}

        # number of results
        len_proc_res = len(processed_results)

        # log mean score for each K
        for _k in metric_valid_k:
            metric_name = f"{metric}_{_k}"
            # aggregated_result[metric_name] = (
            #     sum([r[_k] for r in processed_results]) / len_proc_res
            # )
            aggregated_sum = 0.0
            processed = 0
            # count the number of results for which the value for metric@k is missing
            missing = 0
            missing_counter_name = f"{metric}_{_k}_missing"

            for r in processed_results:
                if _k in r:
                    aggregated_sum += r[_k]
                    processed += 1
                else:
                    missing += 1

            aggregated_result[metric_name] = aggregated_sum / processed

            log_metric(key=metric_name, value=aggregated_result[metric_name])
            log_metric(key=missing_counter_name, value=missing)

    # calculate mean RR
    aggregated_result["MRR"] = sum([r for r in mrr_res]) / len(mrr_res)
    log_metric(key="MRR", value=aggregated_result["MRR"])

    return aggregated_result
