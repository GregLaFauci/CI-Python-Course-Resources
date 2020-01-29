def timed(fn):
    from time import perf_counter
    def inner(*args, **kwargs):
        total_elapsed = 0
        for i in range(10):
            start = perf_counter()
            result = fn(*args, **kwargs)
            end = perf_counter()
            total_elapsed += (end - start)
            print('Run #: {0} took {1:.6f}s'.format(i, total_elapsed))
        avg_run_time = total_elapsed / 10
        print('Avg Run time: {0:.6f}s'.format(avg_run_time))
        return result
    return inner

def calc_fib_recurse(n):
    return 1 if n < 3 else calc_fib_recurse(n-2) + calc_fib_recurse(n-1)

def fib(n):
    return calc_fib_recurse(n)
