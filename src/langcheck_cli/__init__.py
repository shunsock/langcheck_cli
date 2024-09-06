from langcheck_cli.router import Router


def main() -> None:
    controller = Router.route()
    controller.run()
