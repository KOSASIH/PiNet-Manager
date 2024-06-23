import os
import json

class Config:
    def __init__(self):
        self.config_file = 'config.json'
        self.config_data = self.load_config()

    def load_config(self):
        with open(self.config_file, 'r') as f:
            return json.load(f)

    def get(self, key):
        return self.config_data.get(key)

    def set(self, key, value):
        self.config_data[key] = value
        self.save_config()

    def save_config(self):
        with open(self.config_file, 'w') as f:
            json.dump(self.config_data, f, indent=4)
