from unittest.mock import patch

from langcheck_cli.controller.check_metrics import CheckMetrics
from langcheck_cli.controller.help_message import HelpMessage
from langcheck_cli.router import Router


def test_default_evaluation_controller() -> None:
    """
    引数が指定されなかった場合、HelpMessageControllerが返されることをテストします。
    """
    with patch('sys.argv', ['router.py']):
        controller = Router.route()
        assert isinstance(controller, HelpMessage)


def test_evaluation_controller_with_id() -> None:
    """
    -pまたは--pathが指定された場合、CheckMetricsControllerが返されることをテストします。
    """
    with patch('sys.argv', ['router.py', '-p', 'path/to/file']):
        controller = Router.route()
        assert isinstance(controller, CheckMetrics)


def test_help_message_controller() -> None:
    """
    -hまたは--helpが指定された場合、HelpMessageControllerが返されることをテストします。
    """
    with patch('sys.argv', ['router.py', '--help']):
        controller = Router.route()
        assert isinstance(controller, HelpMessage)
