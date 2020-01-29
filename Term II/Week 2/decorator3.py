from functools import wraps

def counter(fn):
    cnt = 0

    @wraps(fn)
    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        print('Function {0} was called {1} times'.format(fn.__name__, cnt))
    
    return inner

@counter
def add(a: int, b: int=10) -> int:
    """
    returns the sum of two integers
    """
    return a + b    