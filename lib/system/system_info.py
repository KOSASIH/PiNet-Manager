import platform

class SystemInfo:
    def __init__(self):
        pass

    def get_system_info(self):
        return platform.uname()
