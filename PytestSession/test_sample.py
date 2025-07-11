import sys

import pytest


def func(x):
    return x + 1

#Pytest skip marker Tutorial
@pytest.mark.skip(reason="Development not completed")
def test_answer():
    assert func(3) == 4

def test_sum():
    assert func(7) == 8

#skipif marker tutorial
@pytest.mark.skipif(sys.platform != "win64",reason = "System not compatible/Windows only-feature")
def test_windows_registry_access():
    assert True