from src.math_operations import add, sub


def test_add():
    assert add(2, 3) == 5
    assert add(3, 0) == 3
    assert add(5, -3) == 2
    assert add(-10, 2) == -8
    assert add(-4, -3) == -7
    assert add(-1, 1) == 0


def test_sub():
    assert sub(5, 5) == 0
    assert sub(5, 3) == 2
    assert sub(2, 5) == -3
    assert sub(1, -1) == 2
    assert sub(-1, -2) == 1
