import json
import os

class PiNetManagerConfig:
    def __init__(self):
        self.api_url = ""
        self.username = ""
        self.password = ""

    def load_config(self, path: str) -> None:
        with open(path, "r") as f:
            config = json.load(f)
            self.api_url = config["api_url"]
            self.username = config["username"]
            self.password = config["password"]

    def save_config(self, path: str) -> None:
       config = {"api_url": self.api_url, "username": self.username, "password": self.password}
        with open(path, "w") as f:
            json.dump(config, f, indent=4)
