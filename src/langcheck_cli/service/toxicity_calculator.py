from typing import List, Optional

import langcheck
import warnings

warnings.filterwarnings("ignore", category=FutureWarning)


class ToxicityCalculator:
    @staticmethod
    def calculate(texts: List[str], threshold: Optional[float]) -> None:
        df = langcheck.metrics.toxicity(texts).to_df()

        # filter by threshold
        if threshold is not None:
            df = df[df["metrics_value"] > threshold]

        print(df)
