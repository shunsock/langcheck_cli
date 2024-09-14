from pathlib import Path
from typing import List, Optional

from langcheck_cli.controller.controller import Controller
from langcheck_cli.service.ai_disclaimer_similarity_calculator import (
    AiDisclaimerSimilarityCalculator,
)
from langcheck_cli.service.get_lines_from_text_file import GetLinesFromTextFile
from langcheck_cli.service.sentiment_calculator import SentimentCalculator
from langcheck_cli.service.toxicity_calculator import ToxicityCalculator
from langcheck_cli.service.fluency_calculator import FluencyCalculator


class Metrics(Controller):
    name: Optional[str] = None
    path: Optional[Path] = None
    threshold: Optional[float] = None
    upper_than: bool = False

    def __init__(self, user_inputs: List[str]) -> None:
        super().__init__()
        Metrics.parse(user_inputs)
        Metrics.validate()

    @staticmethod
    def parse(user_inputs: List[str]) -> None:
        """
        Parse user inputs to set the command and path.
        This method is called internally to parse the user inputs and set the command and path.

        Parameters:
            user_inputs (List[str]): List of user inputs

        Raises:
            ValueError: if a flag is invalid
        """
        # parse user inputs
        index: int = 0
        last_index: int = len(user_inputs) - 1
        while index < last_index:
            # set flag
            flag: str = user_inputs[index]

            # set value
            # this is safe because we are checking the last index
            index += 1
            value: str = user_inputs[index]

            match flag:
                case "-n" | "--name":
                    Metrics.name = value
                case "-f" | "--file":
                    Metrics.path = Path(value)
                case "-u" | "--upper-than":
                    if not value.replace(".", "", 1).isdigit():
                        raise ValueError(f"flag {value} requires a float value")

                    Metrics.threshold = float(value)
                    Metrics.upper_than = True
                case "-l" | "--lower-than":
                    if not value.replace(".", "", 1).isdigit():
                        raise ValueError(f"flag {value} requires a float value")

                    Metrics.threshold = float(value)
                    Metrics.upper_than = False
                case _:
                    raise ValueError(f"flag {flag} is invalid")

            # update index
            index += 1

    @staticmethod
    def validate() -> None:
        """
        Validate the command and path
        This method is called internally to validate the command and path.

        Raises:
            ValueError: if the path is missing
            ValueError: if the path does not exist
            ValueError: if the command is invalid
        """
        # validate for path
        match Metrics.path:
            case None:
                raise ValueError("file path is required")
            case _:
                if not Metrics.path.exists():
                    raise ValueError(f"file {Metrics.path} does not exist")

        # validate for command
        match Metrics.name:
            case None:
                raise ValueError("command is required")
            case "toxicity" | "sentiment" | "ai_disclaimer_similarity" | "fluency":
                pass
            case _:
                raise ValueError(f"command {Metrics.name} is invalid")

    def run(self) -> None:
        texts = GetLinesFromTextFile.read_file_lines(str(Metrics.path))

        match Metrics.name:
            case "toxicity":
                ToxicityCalculator.calculate(
                    texts, Metrics.threshold, Metrics.upper_than
                )
            case "sentiment":
                SentimentCalculator.calculate(
                    texts, Metrics.threshold, Metrics.upper_than
                )
            case "ai_disclaimer_similarity":
                AiDisclaimerSimilarityCalculator.calculate(
                    texts, Metrics.threshold, Metrics.upper_than
                )
            case "fluency":
                FluencyCalculator.calculate(
                    texts, Metrics.threshold, Metrics.upper_than
                )
            case _:
                pass
