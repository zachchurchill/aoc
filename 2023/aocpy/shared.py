import os
import time
from functools import wraps
from typing import Final


INPUTS_DIR: Final[str] = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "inputs"
)


def timer(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        t1 = time.perf_counter()
        f(*args, **kwargs)
        t2 = time.perf_counter()
        print(f"Execution time: {t2 - t1}")
    return wrapper
