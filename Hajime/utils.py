import json


class Messages:
    def __init__(self):
        self.green = '\033[92m'
        self.red = '\033[91m'
        self.end = '\033[0m'

    def message(self, status: int = 200, message: object = ""):
        color = self.green if 200 <= status < 300 else self.red if 400 <= status < 500 else self.end
        print(f"[{color} {status} {self.end}] {message}")

