# open anaconda prompt and change the directory where this script is present and use the command  "py.test -v pytest_example.py"
import math
import pytest
def test_sqrt():
    num = 25
    result = math.sqrt(num)
    assert result == 5 
    return result

def test_equality():
    assert 10 == 15