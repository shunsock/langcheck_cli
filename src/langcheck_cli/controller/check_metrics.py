import langcheck

from langcheck_cli.controller.controller import Controller
from langcheck_cli.service.get_lines_from_text_file import GetLinesFromTextFile


class CheckMetrics(Controller):
    def __init__(self, file_path: str) -> None:
        super().__init__()
        self.file_path = file_path

    def run(self) -> None:
        print("from ImageExtractor")
        lines = GetLinesFromTextFile.read_file_lines(self.file_path)

        tox = langcheck.metrics.fluency(lines).metric_values
        sentiment = langcheck.metrics.sentiment(lines).metric_values

        print(lines)
        print(tox)
        print(sentiment)
