from typing import List


class GetLinesFromTextFile:
    @staticmethod
    def read_file_lines(file_path: str) -> List[str]:
        """
        指定されたファイルを読み込み、行ごとにリストとして返します。

        Args:
            file_path (str): 読み込むファイルのパス。

        Returns:
            List[str]: ファイルの各行を要素とするリスト。
        """
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                lines = file.readlines()
                # 各行の末尾の改行文字を削除したい場合は以下の行を追加
                lines = [line.strip() for line in lines]
            return lines
        except FileNotFoundError:
            raise ValueError(f"Error: The file '{file_path}' was not found.")
