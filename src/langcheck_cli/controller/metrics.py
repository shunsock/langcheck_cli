from pathlib import Path
from typing import List, Optional

from langcheck_cli.controller.controller import Controller


class Metrics(Controller):
    command: Optional[str] = None
    path: Optional[Path] = None

    def __init__(self, user_inputs: List[str]) -> None:
        super().__init__()
        Metrics.parse(user_inputs)
        Metrics.validate()

    @staticmethod
    def parse(user_inputs: List[str]) -> None:
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
        print("from Metrics")
        print(f"command: {Metrics.command}")
        print(f"path: {Metrics.path}")
