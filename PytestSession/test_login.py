#This is a parametrize marker tutorial piece of code
import pytest

def login(username,password):
    if username == "admin" and password == "12345":
        return "login successful"
    elif username != "admin":
        return "wrong username"
    else:
        return "wrong password"


@pytest.mark.parametrize("username,password,expected", [
    ("admin","12345","login successful"),
    ("admin13","12345","wrong username"),
    ("admin","145","wrong password")
])
def test_login(username,password,expected):
    assert login(username,password) == expected