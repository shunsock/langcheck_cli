from typing import List

import langcheck


class AiDisclaimerSimilarityCalculator:
    @staticmethod
    def calculate(texts: List[str]) -> None:
        print(langcheck.metrics.ai_disclaimer_similarity(texts).to_df())
