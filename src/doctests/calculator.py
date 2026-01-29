def sum_two(x: int | float , y: int | float) -> int | float:
    '''
    Docstring for sum_two
    >>> sum_two(10, 10)
    20
    >>> sum_two(-10, 20)
    10
    >>> sum_two('10', 20)
    Traceback (most recent call last):
    ...
    AssertionError: x needs to be int or float
    '''
    assert isinstance(x, (int, float)), 'x needs to be int or float'
    assert isinstance(y, (int, float)), 'y needs to be int or float'
    return x + y

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)