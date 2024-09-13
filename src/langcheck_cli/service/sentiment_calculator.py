import warnings
from typing import List, Optional

import langcheck

warnings.filterwarnings("ignore", category=FutureWarning)


class SentimentCalculator:
    @staticmethod
    def calculate(
        texts: List[str], threshold: Optional[float], upper_than: bool
    ) -> None:
        df = langcheck.metrics.ja.sentiment(texts).to_df()

        # filter by threshold
        if threshold is not None and upper_than is True:
            df = df[df["metric_value"] > threshold]
        if threshold is not None and upper_than is False:
            df = df[df["metric_value"] < threshold]

        print(df[["generated_output", "metric_value"]])
