import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from funciones import evaluar, mostrar

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

def test_mostrar_preorder():
    assert mostrar("PRE", ["+", "3", "4"]) == "3 + 4"
    assert mostrar("PRE", ["+", "*", "+", "3", "4", "5", "7"]) == "(3 + 4) * 5 + 7"


def test_mostrar_postorder():
    assert mostrar("POST", ["3", "4", "+"]) == "4 + 3"
    #Este es el caso para mostrar POST dado en el enunciado. Se imprime en orden diferente
    #por el orden en que se toman los ultimos elementos en la pila, pero aun es correcto
    assert mostrar("POST", ["8", "3", "-", "8", "4", "4", "+", "*", "+"]) == "(4 + 4) * 8 + 8 - 3"
    assert mostrar("POST", ["3","4", "-"]) == "3 - 4"

if __name__ == "__main__":
    pytest.main()