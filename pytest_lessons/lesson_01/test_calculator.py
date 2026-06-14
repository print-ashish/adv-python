from calculator import add, subtract , multiply


def test_add_two_numbers():
    result = add(2, 3)
    assert result == 5


def test_subtract_two_numbers():
    result = subtract(10, 4)
    assert result == 6


def test_multiply_two_numbers():
    result = multiply(3,4)
    assert result == 12

def test_add_negative_numbers():
    result = add(-2,-4)
    assert result == -6

def test_subtract_negative_numbers():
    result = subtract(-2,-4)
    assert result == 2