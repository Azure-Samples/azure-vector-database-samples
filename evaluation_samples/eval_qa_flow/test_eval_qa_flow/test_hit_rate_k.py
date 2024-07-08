import pytest
from src.flows.eval_qa_flow.metrics.calculate_hit_rate_at_k import (
    calculate_hit_rate_at_k,
)


@pytest.mark.parametrize(
    "retrieved, ground_truth, k, expected",
    [
        ([], "a|b|c", [3], {}),
        ([{"source": "d"}, {"source": "e"}], "a|b|c", [3], {3: 0}),
        ([{"source": "d"}, {"source": "e"}], "", [3], {}),
        ([{"source": "d"}, {"source": "m"}], "g|h|j", [1], {1: 0}),
        ([{"source": "d"}, {"source": "m"}], "d", [1, 3, 10], {1: 1, 3: 1, 10: 1}),
        ([{"source": "d"}, {"source": "m"}], "m|k", [1, 3, 10], {1: 0, 3: 1, 10: 1}),
        (
            [{"source": "d"}, {"source": "i"}, {"source": "r"}, {"source": "m"}],
            "m|k",
            [1, 3, 10],
            {1: 0, 3: 0, 10: 1},
        ),
    ],
)
def test_hit_rate_at_k(
    retrieved: list[dict], ground_truth: str, k: list[int], expected: dict
):
    """Test hit rate @K

    Args:
        retrieved (list[dict]): Retrieved documents from the search engine
        ground_truth (str): List of ground truth URLs
        expected (float): Expected hit rate value
    """
    hit_rate_k = calculate_hit_rate_at_k(retrieved, ground_truth, k)
    # for empty results
    if expected == {}:
        assert hit_rate_k == {}

    # for non-empty results, test floats
    for key in hit_rate_k.keys():
        assert hit_rate_k[key] == pytest.approx(expected[key], 0.0001)
