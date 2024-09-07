from unittest.mock import patch

from langcheck_cli.controller.argument import Argument
from langcheck_cli.controller.help_message import HelpMessage
from langcheck_cli.controller.metrics import Metrics
from langcheck_cli.router import Router


def test_default_evaluation_controller() -> None:
    """
    引数が指定されなかった場合、HelpMessageControllerが返されることをテストします。
    """
    with patch('sys.argv', ['router.py']):
        controller = Router.route()
        assert isinstance(controller, HelpMessage)


def test_help_option_evaluation_controller() -> None:
    """
    引数に-hか--helpが指定された場合、HelpMessageControllerが返されることをテストします。
    """
    with patch('sys.argv', ['router.py', '-h']):
        controller = Router.route()
        assert isinstance(controller, HelpMessage)

    with patch('sys.argv', ['router.py', '--help']):
        controller = Router.route()
        assert isinstance(controller, HelpMessage)


def test_argument_option_evaluation_controller() -> None:
    """
    引数にargumentが指定された場合、ArgumentControllerが返されることをテストします。
    """
    with patch('sys.argv', ['router.py', 'argument']):
        controller = Router.route()
        assert isinstance(controller, Argument)


def test_metrics_option_evaluation_controller() -> None:
    """
    引数にmetricsが指定された場合、MetricsControllerが返されることをテストします。
    """
    with patch('sys.argv', ['router.py', 'metrics']):
        controller = Router.route()
        assert isinstance(controller, Metrics)
