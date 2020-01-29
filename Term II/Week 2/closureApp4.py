def counter(inital_value):

    def inc(increment=1):
        nonlocal inital_value
        inital_value += increment
        return inital_value
    
    return inc

