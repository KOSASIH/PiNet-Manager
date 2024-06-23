# utils.py
import logging
import os

def setup_logging():
    logging.basicConfig(level=logging.INFO)
    logging.info("Logging setup complete")

def get_env_var(var_name: str) -> str:
    return os.environ.get(var_name)
