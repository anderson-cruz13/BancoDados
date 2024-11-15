from typing import List
from datetime import datetime


class Files:
    def __init__(self):
        self._files = []

    def read(self, file) -> None:
        try:
            with open(file, "r") as f:
                for line in f:

                    parts = line.strip().split(",")
                    if len(parts) == 2:
                        name = parts[0].strip()
                        birth_date = parts[1].strip()

                        try:
                            converted_date = datetime.strptime(
                                birth_date, "%d/%m/%Y").strftime("%Y-%m-%d")
                            self._files.append((name, converted_date))
                        except ValueError:
                            return None

        except FileNotFoundError:
            return None

    def write(self, file, content) -> None:
        with open(file, "a") as f:
            f.write(content)

    @property
    def files(self) -> List[str]:
        return self._files


if __name__ == "__main__":
    f = Files()
    f.read("users.txt")
    print(f.files)
