from typing import List


class Files:
    def __init__(self):
        self._files = []

    def read(self, file) -> None:
        try:
            with open(file, "r") as f:
                content = f.read()
                self._files.append(content)
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
    f.read("test.txt")
    print(f.files)
