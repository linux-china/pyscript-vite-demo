# js module stub for python: `from js import console, window`
class Console:
    def log(self, message):
        pass


class Window:
    console: Console


def fetch(url: str, options: dict):
    pass


def addEventListener(event: str, callback: callable):
    pass


def dispatchEvent(event: str):
    pass


window = Window()
console = Console()
