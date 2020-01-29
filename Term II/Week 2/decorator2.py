def counter(fn):
    cnt = 0
    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        print('Function {0} was called {1} times'.format(fn.__name__, cnt))
    inner.__name__ = fn.__name__
    inner.__doc__ = fn.__doc__
    return inner

@counter
def add(a: int, b: int=10) -> int:
    """
    returns the sum of two integers
    """
    return a + b    