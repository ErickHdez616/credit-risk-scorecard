from scorecard.evaluate import gini


def test_gini_perfect_model():
    assert gini([0, 0, 1, 1], [0.1, 0.2, 0.8, 0.9]) == 1.0
