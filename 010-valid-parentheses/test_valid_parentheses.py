import pytest
from valid_parentheses import valid_parentheses

def test_single_pair():
    # Testa um único par válido
    assert valid_parentheses("()") == True

def test_multiple_types():
    # Testa múltiplos tipos de colchetes corretamente aninhados
    assert valid_parentheses("({[]})") == True

def test_invalid_order():
    # Testa colchetes em ordem incorreta
    assert valid_parentheses("{[}]") == False

def test_unmatched_open():
    # Testa colchetes abertos sem correspondência
    assert valid_parentheses("({[") == False

def test_unmatched_close():
    # Testa colchetes fechados sem correspondência
    assert valid_parentheses("({})]") == False
