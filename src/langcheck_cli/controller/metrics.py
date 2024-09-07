from pathlib import Path
from typing import List, Optional

from langcheck_cli.controller.controller import Controller
from langcheck_cli.service.ai_disclaimer_similarity_calculator import (
    AiDisclaimerSimilarityCalculator,
)
from langcheck_cli.service.get_lines_from_text_file import GetLinesFromTextFile
from langcheck_cli.service.sentiment_calculator import SentimentCalculator
from langcheck_cli.service.toxicity_calculator import ToxicityCalculator


class Metrics(Controller):
    command: Optional[str] = None
    path: Optional[Path] = None

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
                case "-c" | "--command":
                    Metrics.command = value
                case "-f" | "--file":
                    Metrics.path = Path(value)
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
        match Metrics.command:
            case None:
                raise ValueError("command is required")
            case "toxicity" | "sentiment" | "ai_disclaimer_similarity":
                pass
            case _:
                raise ValueError(f"command {Metrics.command} is invalid")

    def run(self) -> None:
        texts = GetLinesFromTextFile.read_file_lines(str(Metrics.path))

        match Metrics.command:
            case "toxicity":
                ToxicityCalculator.calculate(texts)
            case "sentiment":
                SentimentCalculator.calculate(texts)
            case "ai_disclaimer_similarity":
                AiDisclaimerSimilarityCalculator.calculate(texts)
            case _:
                pass
