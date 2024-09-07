from typing import List

from langcheck_cli.controller.controller import Controller


class Argument(Controller):
    def __init__(self, user_inputs: List[str]) -> None:
        super().__init__()
        self.user_inputs = user_inputs

    def run(self) -> None:
        print("this feature is not implemented yet")
