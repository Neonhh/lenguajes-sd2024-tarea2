import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from aritmethic_order import handle_action, main  # Import functions from aritmethic_order.py

def test_handle_action_eval(capsys):
    # Test EVAL command
    handle_action(["EVAL", "PRE", "+", "3", "4"])
    captured = capsys.readouterr()
    assert captured.out.strip() == "7"
    
    handle_action(["EVAL", "POST", "3", "4", "+"]) == 7
    captured = capsys.readouterr()
    assert captured.out.strip() == "7"

def test_handle_action_mostrar(capsys):
    # Test MOSTRAR command
    handle_action(["MOSTRAR", "PRE", "+", "3", "4"])
    captured = capsys.readouterr()
    assert captured.out.strip() == "3 + 4"
    
    handle_action(["MOSTRAR", "POST", "3", "4", "+"])
    captured = capsys.readouterr()
    assert captured.out.strip() == "4 + 3"

def test_handle_action_invalid():
    # Test invalid command
    assert handle_action(["INVALID", "PRE", "+", "3", "4"]) is None

def test_main(monkeypatch, capsys):
    # Test main function with input
    inputs = iter(["EVAL PRE + 3 4", "MOSTRAR PRE + 3 4", "SALIR"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "Inicio del programa aritmethic_order" in captured.out
    assert "7" in captured.out
    assert "3 + 4" in captured.out