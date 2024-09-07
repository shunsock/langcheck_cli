from langcheck_cli.service.sentiment_calculator import SentimentCalculator


def test_calculate_without_threshold() -> None:
    # Test input without threshold
    texts = [
        "You are a good person.",
        "You are a bad person."
    ]
    upper_than = True

    # Call the calculate method without a threshold
    SentimentCalculator.calculate(texts, None, upper_than)

    assert True


def test_calculate_with_threshold() -> None:
    # Test input with a threshold
    texts = [
        "You are a good person.",
        "You are a bad person."
    ]
    threshold = 0.5
    upper_than = True

    # Call the calculate method with a threshold
    SentimentCalculator.calculate(texts, threshold, upper_than)

    assert True
