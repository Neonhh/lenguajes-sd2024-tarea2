import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from funciones import evaluar

def test_evaluar_preorder():
    assert evaluar("PRE", ["+", "3", "4"]) == 7
    assert evaluar("PRE", ["*", "+", "2", "3", "4"]) == 20
    assert evaluar("PRE", ["-", "/", "10", "+", "1", "1", "*", "1", "2"]) == 2
    assert evaluar("PRE", ["+", "*", "2", "3", "4"]) == 10

def test_evaluar_postorder():
    assert evaluar("POST", ["3", "4", "+"]) == 7
    assert evaluar("POST", ["2", "3", "+", "4", "*"]) == 20
    assert evaluar("POST", ["10", "1", "1", "+", "/", "1", "2", "*", "-"]) == 3
    assert evaluar("POST", ["2", "3", "*", "4", "+"]) == 10

def test_invalid_order():
    assert evaluar("INVALID", ["3", "4", "+"]) is None

if __name__ == "__main__":
    pytest.main()