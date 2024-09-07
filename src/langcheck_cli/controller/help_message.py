from langcheck_cli.controller.controller import Controller


class HelpMessage(Controller):
    def __init__(self) -> None:
        super().__init__()

    def run(self) -> None:
        message = """
        Usage: uv run langcheck_cli [options] [sub_commend] ...
        Options:
            -h, --help      show help message
        
        Subcommands:
            metrics         show metrics of the target
                Options for metrics:
                    -n, --name          metrics
                    -f, --file          file path
                    -u, --upper-than    show metrics of the target that is upper than the value
                    -l, --lower-than    show metrics of the target that is lower than the value
        """
        print(message)
