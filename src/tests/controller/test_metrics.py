from pathlib import Path

import pytest

from langcheck_cli.controller.metrics import Metrics


@pytest.fixture(autouse=True)
def reset_metrics():
    """Fixture to reset Metrics attributes before each test."""
    Metrics.name = None
    Metrics.path = None


@pytest.fixture
def temp_file(tmp_path) -> Path:
    """Fixture to create and return a temporary file for testing."""
    temp_file = tmp_path / "test.txt"
    temp_file.write_text("Temporary test file")
    return temp_file


def test_parse_valid_input_command_and_file_short_flags(temp_file) -> None:
    # Test valid input with short flags
    user_inputs = ["-n", "toxicity", "-f", str(temp_file)]
    Metrics.parse(user_inputs)
    assert Metrics.name == "toxicity"
    assert Metrics.path == Path(temp_file)


def test_parse_valid_input_command_and_file_long_flags(temp_file) -> None:
    # Test valid input with long flags
    user_inputs = ["--name", "sentiment", "--file", str(temp_file)]
    Metrics.parse(user_inputs)
    assert Metrics.name == "sentiment"
    assert Metrics.path == Path(temp_file)


def test_parse_invalid_flag() -> None:
    # Test invalid flag
    user_inputs = ["-x", "value"]
    with pytest.raises(ValueError, match="flag -x is invalid"):
        Metrics.parse(user_inputs)


def test_validate_missing_path() -> None:
    # Test missing path validation
    Metrics.name = "toxicity"
    Metrics.path = None
    with pytest.raises(ValueError, match="file path is required"):
        Metrics.validate()


def test_validate_non_existent_file() -> None:
    # Test path that does not exist
    Metrics.name = "toxicity"
    Metrics.path = Path("non_existent_file.txt")
    with pytest.raises(ValueError, match="file non_existent_file.txt does not exist"):
        Metrics.validate()


def test_validate_missing_command(temp_file) -> None:
    # Test missing command validation
    Metrics.name = None
    Metrics.path = temp_file
    with pytest.raises(ValueError, match="command is required"):
        Metrics.validate()


def test_validate_invalid_command(temp_file) -> None:
    # Test invalid command
    Metrics.name = "invalid_command"
    Metrics.path = temp_file
    with pytest.raises(ValueError, match="command invalid_command is invalid"):
        Metrics.validate()


def test_validate_valid_command_and_path(temp_file) -> None:
    # Test valid command and path
    Metrics.name = "sentiment"
    Metrics.path = temp_file
    try:
        Metrics.validate()  # Should not raise any exceptions
    except ValueError as e:
        pytest.fail(f"validate() raised ValueError unexpectedly: {e}")
