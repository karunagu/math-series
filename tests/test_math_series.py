from math_series import __version__
from math_series.series import fibonacci


def test_version():
    assert __version__ == '0.1.0'

def test_fib_zero():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected

def test_fib_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def test_fib_two():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected

def test_fib_three():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected

def test_fib_nine():
    actual = fibonacci(9)
    expected = 34
    assert actual == expected

def test_fib_fourteen():
    actual = fibonacci(14)
    expected = 377
    assert actual == expected
