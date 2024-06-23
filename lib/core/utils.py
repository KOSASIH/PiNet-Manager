import os
import time

class Utils:
    def __init__(self):
        pass

    def get_current_time(self):
        return time.strftime('%Y-%m-%d %H:%M:%S')

    def get_system_info(self):
        return os.uname()

    def execute_command(self, command):
        return os.system(command)
