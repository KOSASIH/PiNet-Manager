# Importing necessary modules and setting up the test utils package
from importlib import import_module
from typing import List, Dict, Any

__all__ = ['test_helpers', 'test_fixtures']

def load_test_modules() -> List[str]:
    """Loads all test modules in the test_utils package"""
    modules = []
    for module in __all__:
        modules.append(import_module(f'test_utils.{module}'))
    return modules

def get_test_fixtures() -> Dict[str, Any]:
    """Returns a dictionary of test fixtures"""
    from.test_fixtures import *
    return {name: obj for name, obj in globals().items() if not name.startswith('__')}

def get_test_helpers() -> Dict[str, Any]:
    """Returns a dictionary of test helpers"""
    from.test_helpers import *
    return {name: obj for name, obj in globals().items() if not name.startswith('__')}
