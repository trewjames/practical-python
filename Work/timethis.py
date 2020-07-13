from time import time


def timethis(func):
    def wrapper(*args, **kwargs):
        start = time()
        try:
            return func(*args, **kwargs)
        finally:
            end = time()
            print(f"{func.__module__}, {func.__name__}, {end-start}")
    return wrapper
