import pytest

from steps import steps
# Supondo que sua função seja definida como steps(n)

def test_single_step():
    # Testa a escada com 1 degrau
    assert steps(1) == ["#"]

def test_two_steps():
    # Testa a escada com 2 degraus
    assert steps(2) == ["# ", "##"]

def test_five_steps():
    # Testa a escada com 5 degraus
    assert steps(5) == ["#    ", "##   ", "###  ", "#### ", "#####"]

def test_zero_steps():
    # Testa a escada com 0 degraus (caso limite)
    assert steps(0) == []

def test_large_steps():
    # Testa a escada com 10 degraus
    assert steps(10) == [
        "#         ",
        "##        ",
        "###       ",
        "####      ",
        "#####     ",
        "######    ",
        "#######   ",
        "########  ",
        "######### ",
        "##########"
    ]
