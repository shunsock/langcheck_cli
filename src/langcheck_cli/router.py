import sys

from langcheck_cli.controller.check_metrics import CheckMetrics
from langcheck_cli.controller.controller import Controller
from langcheck_cli.controller.help_message import HelpMessage


class Router:
    @staticmethod
    def route() -> Controller:

        if len(sys.argv) < 2:
            return HelpMessage()

        option: str = sys.argv[1]

        match option:
            case "-h" | "--help":
                return HelpMessage()
            case "-p" | "--path":
                if len(sys.argv[2]) < 3:
                    raise ValueError(
                        "input values are too short. use -h or --help options"
                    )

                return CheckMetrics(sys.argv[2])
            case _:
                raise ValueError("input values are invalid. use -h or --help options")
