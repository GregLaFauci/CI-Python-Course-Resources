from time import perf_counter


class Timer:
    def __init__(self):
        self.start = perf_counter()
    def __call__(self):
        return perf_counter() - self.start



def timer():
    start = perf_counter()
    def poll():
        return perf_counter() - start
    return poll
