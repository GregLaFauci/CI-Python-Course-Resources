def counter(fn):
    cnt = 0
    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        print('Function {0} was called {1} times'.format(fn.__name__, cnt))
        return fn(*args, **kwargs)
    return inner

def add(a, b=0):
    """
    returns the sum of a and b
    """
    return a + b

@counter
def mult(a: float, b: float=1, c: float=1) -> float:
    """
    returns the product of a, b, and c as a float
    """
    return a * b * c
    