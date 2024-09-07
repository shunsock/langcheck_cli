.PHONY: prepare example

prepare:
	# linting syntax & formatting
	uvx ruff@latest check --fix .
	# type checking for application
	uvx mypy@latest ./src/langcheck_cli --strict --config-file ./mypy.ini
	# formatting with black
	uvx black@latest ./src/langcheck_cli
	# formatting import order
	uvx ruff@latest check --select I --fix .
	# run tests
	uv run pytest src/tests

example:
	uv run langcheck metrics --file ./example/ai_disclaimer.txt -n ai_disclaimer_similarity
	uv run langcheck metrics --file ./example/sentiment.txt -n sentiment -u 0.5
	uv run langcheck metrics --file ./example/toxicity.txt -n toxicity -l 0.3
