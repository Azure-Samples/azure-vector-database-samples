import pytest
from src.flows.eval_qa_flow.metrics.calculate_mrr import calculate_rr


@pytest.mark.parametrize(
    "retrieved, ground_truth, expected",
    [
        ([], "a|b|c", 0),
        ([{"source": "d"}, {"source": "e"}], "a|b|c", 0),
        ([{"source": "d"}, {"source": "e"}], "", 0),
        ([{"source": "d"}, {"source": "e"}], "d|b|c", 1),
        ([{"source": "d"}, {"source": "e"}], "e|b|c", 0.5),
        ([{"source": "d"}, {"source": "e"}], "a|e|c", 0.5),
        ([{"source": "d"}, {"source": "e"}], "d|e|c", 1),
        ([{"source": "d"}, {"source": "e"}], "h|e|d", 1),
        ([{"source": "m"}, {"source": "e"}], "h|e|d", 0.5),
        ([{"source": "m"}, {"source": "e"}, {"source": "n"}], "n", 1 / 3),
        ([{"source": "m"}, {"source": "e"}, {"source": "n"}], "m|n", 1),
    ],
)
def test_reciprocal_rank(retrieved: list[dict], ground_truth: str, expected: float):
    """Test reciprocal rank calculation

    Args:
        retrieved (list[dict]): Retrieved documents from the search engine
        ground_truth (str): List of ground truth URLs
        expected (float): Expected RR value
    """
    rr = calculate_rr(retrieved, ground_truth)
    assert rr == pytest.approx(expected, 0.0001)
