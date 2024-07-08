import pytest
from src.flows.eval_qa_flow.metrics.calculate_recall_at_k import (
    calculate_recall_at_k,
)


@pytest.mark.parametrize(
    "retrieved, ground_truth, k, expected",
    [
        ([], "a|b|c", [3], {3: 0}),
        ([{"source": "d"}, {"source": "e"}], "a|b|c", [1], {1: 0}),
        ([{"source": "d"}, {"source": "e"}], "", [3], {}),
        ([{"source": "d"}, {"source": "m"}], "g|h|j", [3], {3: 0}),
        ([{"source": "d"}, {"source": "m"}], "d", [1, 3, 10], {1: 1, 3: 1, 10: 1}),
        (
            [{"source": "d"}, {"source": "a"}, {"source": "d"}],
            "d|a",
            [1, 3, 10],
            {1: 0.5, 3: 1, 10: 1},
        ),
        (
            [{"source": "d"}, {"source": "a"}, {"source": "n"}],
            "a|d|n",
            [1, 2, 10],
            {1: 1 / 3, 2: 2 / 3, 10: 1},
        ),
    ],
)
def test_calculate_recall_at_k(
    retrieved: list[dict], ground_truth: str, k: list[int], expected: dict
):
    """Test recall @K

    Args:
        retrieved (list[dict]): Retrieved documents from the search engine
        ground_truth (str): List of ground truth URLs
        expected (float): Expected Recall@K value
    """
    recall_k = calculate_recall_at_k(retrieved, ground_truth, k)
    # for empty results
    if expected == {}:
        assert recall_k == {}

    # for non-empty results, test floats
    for key in recall_k.keys():
        assert recall_k[key] == pytest.approx(expected[key], 0.0001)
