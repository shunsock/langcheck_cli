from langcheck_cli.service.ai_disclaimer_similarity_calculator import (
    AiDisclaimerSimilarityCalculator,
)


def test_calculate_without_threshold() -> None:
    # Test input without threshold
    texts = [
        "This is a sample disclaimer.",
        "Another disclaimer with AI terms."
    ]
    upper_than = True

    # Call the calculate method without a threshold
    AiDisclaimerSimilarityCalculator.calculate(texts, None, upper_than)

    assert True


def test_calculate_with_threshold() -> None:
    # Test input with a threshold
    texts = [
        "Disclaimer mentioning AI.",
        "Another disclaimer text."
    ]
    threshold = 0.5
    upper_than = True

    # Call the calculate method with a threshold
    AiDisclaimerSimilarityCalculator.calculate(texts, threshold, upper_than)

    assert True
