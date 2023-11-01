import pytest

from app.utils.fibonacci import calculate_fibonacci


def test_calculate_fibonacci():
    assert calculate_fibonacci(1) == 1
    assert calculate_fibonacci(2) == 1
    assert calculate_fibonacci(3) == 2
    assert calculate_fibonacci(10) == 55
    assert calculate_fibonacci(20) == 6765


def test_calculate_fibonacci_negative_input():
    with pytest.raises(ValueError) as excinfo:
        calculate_fibonacci(-1)
    assert str(excinfo.value) == "Input should be a positive integer"


def test_calculate_fibonacci_zero_input():
    with pytest.raises(ValueError) as excinfo:
        calculate_fibonacci(0)
    assert str(excinfo.value) == "Input should be a positive integer"
