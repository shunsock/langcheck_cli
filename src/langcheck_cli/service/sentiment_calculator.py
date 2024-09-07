from typing import List

import langcheck
import warnings

warnings.filterwarnings("ignore", category=FutureWarning)


class SentimentCalculator:
    @staticmethod
    def calculate(texts: List[str]) -> None:
        print(langcheck.metrics.sentiment(texts).to_df())
