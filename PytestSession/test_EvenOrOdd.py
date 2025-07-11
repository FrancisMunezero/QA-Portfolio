import pytest


def even_or_odd(x):
    if x%2 == 0:
        return "Even"
    else:
        return "odd"

@pytest.mark.smoke
def test_even():
    result = even_or_odd(6)
    print(f"The number is: {result}")

@pytest.mark.regression
def test_odd():
    result = even_or_odd(135224467)
    assert result == "odd", "Number is not odd"

def test_large_even_num():
    result = even_or_odd(263547264576)
    assert result == "Even", "263547264576 must be Even"