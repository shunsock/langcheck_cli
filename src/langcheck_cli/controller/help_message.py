from langcheck_cli.controller.controller import Controller


class HelpMessage(Controller):
    def __init__(self) -> None:
        super().__init__()

    def run(self) -> None:
        message = """
        Usage: uv run langcheck_cli [options] [target] ...
        Options:
            -h, --help      show help message
            -u, --url       source url to extract images
        """
        print(message)
