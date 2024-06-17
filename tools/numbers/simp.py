def add(a, b):
    global function_called
    function_called = True
    return a + b

def subtract(a, b):
    global function_called
    function_called = True
    return a - b