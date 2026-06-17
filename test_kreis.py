# Datei: test_kreis.py
import math
import pytest
from kreis_funktion import durchmesser, umfang, fläche

def test_durchmesser():
    assert durchmesser(5) == 10

def test_umfang():
    assert umfang(1) == pytest.approx(2 * math.pi)

def test_flaeche():
    assert fläche(2) == pytest.approx(4 * math.pi)