import pytest
from src.flows.eval_qa_flow.metrics.calculate_precision_at_k import (
    calculate_precision_at_k,
)


@pytest.mark.parametrize(
    "retrieved, ground_truth, k, expected",
    [
        ([], "a|b|c", [3], {}),
        ([{"source": "d"}, {"source": "e"}], "a|b|c", [3], {3: 0}),
        ([{"source": "d"}, {"source": "e"}], "", [3], {}),
        ([{"source": "d"}, {"source": "m"}], "g|h|j", [3], {3: 0}),
        ([{"source": "d"}, {"source": "m"}], "d", [1, 3, 10], {1: 1, 3: 0.5, 10: 0.5}),
        (
            [{"source": "d"}, {"source": "m"}, {"source": "a"}],
            "d",
            [1, 2],
            {1: 1, 2: 1 / 2, 10: 1 / 3},
        ),
        (
            [{"source": "d"}, {"source": "b"}, {"source": "a"}],
            "a|b",
            [1, 2, 3],
            {1: 0, 2: 1 / 2, 3: 2 / 3},
        ),
        (
            [{"source": "d"}, {"source": "d"}, {"source": "m"}],
            "d",
            [1, 2, 3],
            {1: 1, 2: 1, 3: 2 / 3},
        ),
    ],
)
def test_precision_k(
    retrieved: list[dict], ground_truth: str, k: list[int], expected: dict
):
    """Test precision @K

    Args:
        retrieved (list[dict]): Retrieved documents from the search engine
        ground_truth (str): List of ground truth URLs
        expected (float): Expected RR value
    """
    precision_k = calculate_precision_at_k(retrieved, ground_truth, k)
    # for empty results
    if expected == {}:
        assert precision_k == {}

    # for non-empty results, test floats
    for key in precision_k.keys():
        assert precision_k[key] == pytest.approx(expected[key], 0.0001)


# This test should fail, marking to make sure assertion works properly
@pytest.mark.xfail(run=True)
@pytest.mark.parametrize(
    "retrieved, ground_truth, k, expected",
    [
        (
            [{"source": "d"}, {"source": "b"}, {"source": "a"}],
            "a|b",
            [1, 2, 3],
            {
                1: 0,
                2: 1 / 2,
                3: 2 / 8,
            },  # giving incorrect answer to make sure test fails as expected
        ),
    ],
)
def test_precision_k_should_fail(
    retrieved: list[dict], ground_truth: str, k: list[int], expected: dict
):
    """Test precision @K

    Args:
        retrieved (list[dict]): Retrieved documents from the search engine
        ground_truth (str): List of ground truth URLs
        expected (float): Expected Precision@K value
    """
    precision_k = calculate_precision_at_k(retrieved, ground_truth, k)
    # for empty results
    if expected == {}:
        assert precision_k == {}

    # for non-empty results, test floats
    for key in precision_k.keys():
        assert precision_k[key] == pytest.approx(expected[key], 0.0001)
