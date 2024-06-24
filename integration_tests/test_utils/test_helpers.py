# Advanced test helpers with cutting-edge features
import pytest
from typing import Any, Callable

def async_test(func: Callable) -> Callable:
    """Decorator to run a test function asynchronously"""
    async def wrapper(*args, **kwargs):
        return await func(*args, **kwargs)
    return wrapper

def mock_api_response(response: Any) -> Callable:
    """Decorator to mock API responses"""
    def decorator(func: Callable):
        @pytest.fixture
        def mock_response():
            return response
        return func(mock_response)
    return decorator

def retry_on_failure(max_retries: int = 3) -> Callable:
    """Decorator to retry a test function on failure"""
    def decorator(func: Callable):
        def wrapper(*args, **kwargs):
            for _ in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Retry {_+1}/{max_retries} failed: {e}")
            raise Exception("All retries failed")
        return wrapper
    return decorator

def measure_execution_time(func: Callable) -> Callable:
    """Decorator to measure the execution time of a test function"""
    import time
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.2f} seconds")
        return result
    return wrapper
