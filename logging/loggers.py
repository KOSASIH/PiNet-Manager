# loggers.py
import logging

# Custom Logger Class with Advanced Features
class PiNetManagerLogger(logging.Logger):
    def __init__(self, name: str):
        super().__init__(name)
        self.setLevel(logging.DEBUG)

    def debug(self, msg: str, *args, **kwargs):
        # Custom debug logging with additional metadata
        self.log(logging.DEBUG, msg, *args, **kwargs, extra={'metadata': {'component': 'PiNetManager'}})

    def info(self, msg: str, *args, **kwargs):
        # Custom info logging with additional metadata
        self.log(logging.INFO, msg, *args, **kwargs, extra={'metadata': {'component': 'PiNetManager'}})

    def warning(self, msg: str, *args, **kwargs):
        # Custom warning logging with additional metadata
        self.log(logging.WARNING, msg, *args, **kwargs, extra={'metadata': {'component': 'PiNetManager'}})

    def error(self, msg: str, *args, **kwargs):
        # Custom error logging with additional metadata
        self.log(logging.ERROR, msg, *args, **kwargs, extra={'metadata': {'component': 'PiNetManager'}})

    def critical(self, msg: str, *args, **kwargs):
        # Custom critical logging with additional metadata
        self.log(logging.CRITICAL, msg, *args, **kwargs, extra={'metadata': {'component': 'PiNetManager'}})

# Create a custom logger instance
logger = PiNetManagerLogger('pinet_manager')
