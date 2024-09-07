from typing import List

import langcheck


class SentimentCalculator:
    @staticmethod
    def calculate(texts: List[str]) -> None:
        print(langcheck.metrics.sentiment(texts).to_df())
