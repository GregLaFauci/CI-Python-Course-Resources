def upperCaseFunc(str):
    return str.upper()

def funcNoDecor(str):
    ''' 
    This is an undecorated function
    '''
    return str + str

@upperCaseFunc
def funcDecor(str):
    '''
    This is a decorated function
    '''
    return str + str

def mainFunc(fn):
    return fn

