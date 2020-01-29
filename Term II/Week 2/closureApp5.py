def counter(fn):
    cnt = 0

    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        print('{0} has been called {1} times'.format(fn.__name__, cnt))
        return fn(*args, **kwargs)

    return inner

def add(a,b):
    return a + b

def mult(a,b,c):
    return a * b * c
    