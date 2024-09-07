from typing import List

import langcheck
import warnings

warnings.filterwarnings("ignore", category=FutureWarning)


class ToxicityCalculator:
    @staticmethod
    def calculate(texts: List[str]) -> None:
        print(langcheck.metrics.toxicity(texts).to_df())
