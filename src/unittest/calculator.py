def sum_two(x: int | float , y: int | float) -> int | float:
    assert isinstance(x, (int, float)), 'x needs to be int or float'
    assert isinstance(y, (int, float)), 'y needs to be int or float'
    return x + y