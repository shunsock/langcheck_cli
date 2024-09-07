from langcheck_cli.service.toxicity_calculator import ToxicityCalculator


def test_calculate_without_threshold() -> None:
    # Test input without threshold
    texts = [
        "good, this is a good idea."
        "This is stupid; it doesn't work completely."
    ]
    upper_than = True

    # Call the calculate method without a threshold
    ToxicityCalculator.calculate(texts, None, upper_than)

    assert True


def test_calculate_with_threshold() -> None:
    # Test input with a threshold
    texts = [
        "good, this is a good idea."
        "This is stupid; it doesn't work completely."
    ]
    threshold = 0.5
    upper_than = True

    # Call the calculate method with a threshold
    ToxicityCalculator.calculate(texts, threshold, upper_than)

    assert True
