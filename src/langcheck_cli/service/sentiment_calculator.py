from typing import List, Optional

import langcheck
import warnings

warnings.filterwarnings("ignore", category=FutureWarning)


class SentimentCalculator:
    @staticmethod
    def calculate(texts: List[str], threshold: Optional[float]) -> None:
        df = langcheck.metrics.sentiment(texts).to_df()

        # filter by threshold
        if threshold is not None:
            df = df[df["metrics_value"] > threshold]

        print(df)
