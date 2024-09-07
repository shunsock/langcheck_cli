from unittest.mock import patch

from langcheck_cli.controller.argument import Argument
from langcheck_cli.controller.help_message import HelpMessage
from langcheck_cli.controller.metrics import Metrics
from langcheck_cli.router import Router


def test_default_evaluation_controller() -> None:
    """
    test return HelpMessageController when no arguments are specified
    """
    with patch('sys.argv', ['router.py']):
        controller = Router.route()
        assert isinstance(controller, HelpMessage)


def test_help_option_evaluation_controller() -> None:
    """
    test return HelpMessageController when -h or --help is specified as an argument
    """
    with patch('sys.argv', ['router.py', '-h']):
        controller = Router.route()
        assert isinstance(controller, HelpMessage)

    with patch('sys.argv', ['router.py', '--help']):
        controller = Router.route()
        assert isinstance(controller, HelpMessage)


def test_argument_option_evaluation_controller() -> None:
    """
    test return ArgumentController when argument is specified as an argument
    """
    with patch('sys.argv', ['router.py', 'argument']):
        controller = Router.route()
        assert isinstance(controller, Argument)


def test_metrics_option_evaluation_controller() -> None:
    """
    test return MetricsController when metrics is specified as an argument
    """
    with patch('sys.argv', ['router.py', 'metrics', '-n', 'toxicity', '-f', 'README.md']):
        controller = Router.route()
        assert isinstance(controller, Metrics)
