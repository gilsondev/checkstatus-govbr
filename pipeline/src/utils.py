from collections.abc import Callable
from functools import wraps
from random import randint
from time import sleep

from loguru import logger


def delay_call(min: int, max: int) -> Callable:
    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            sleep_time = randint(min, max)
            func(*args, **kwargs)
            logger.debug(f"Sleeping {func.__name__} in {sleep_time} sec.")
            sleep(sleep_time)

        return wrapper

    return decorate
