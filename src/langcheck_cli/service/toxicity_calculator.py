from typing import List

import langcheck


class ToxicityCalculator:
    @staticmethod
    def calculate(texts: List[str]) -> None:
        print(langcheck.metrics.toxicity(texts).to_df())
