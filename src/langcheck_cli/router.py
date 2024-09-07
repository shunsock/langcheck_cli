import sys

from langcheck_cli.controller.argument import Argument
from langcheck_cli.controller.controller import Controller
from langcheck_cli.controller.help_message import HelpMessage
from langcheck_cli.controller.metrics import Metrics


class Router:
    @staticmethod
    def route() -> Controller:

        if len(sys.argv) < 2:
            return HelpMessage()

        option: str = sys.argv[1]

        match option:
            case "-h" | "--help":
                return HelpMessage()
            case "argument":
                return Argument(sys.argv[2:])
            case "metrics":
                return Metrics(sys.argv[2:])
            case _:
                raise ValueError("input values are invalid. use -h or --help options")
