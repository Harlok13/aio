import time
from typing import Callable, Any
import functools
import asyncio


def async_timed():
    def wrapper(func: Callable) -> Callable:

        @functools.wraps(func)
        async def wrapped(*args, **kwargs) -> Any:

            print(f'выполняется {func} с аргументами {args} {kwargs}')
            start = time.time()
            try:
                return await func(*args, **kwargs)
            finally:
                end = time.time()
                total = end - start
                print(f'{func} завершилась за {total:.4f} с')

        return wrapped

    return wrapper
