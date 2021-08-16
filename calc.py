
def add(a, b):
    """Addition Function"""
    return a + b


def sub(a, b):
    """Subtraction Function"""
    return a - b


def mul(a, b):
    """Multiplication Function"""
    return a * b


def div(a, b):
    """Division FUnction"""
    if b == 0:
        raise ValueError('Can not divide with zero')
    else:
        return a / b
