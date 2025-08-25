import pytest
from src.magiczne_kwadraty import magicznyKwadrat

def test_odd_square():
    kw = magicznyKwadrat(3)
    kw.uzupelnij()
    wyniki = kw.podsumowanie()

    # Sprawdź czy suma wierszy, kolumn i przekątnych jest taka sama
    assert all(s == wyniki["suma_wierszy"][0] for s in wyniki["suma_wierszy"])
    assert all(s == wyniki["suma_kolumn"][0] for s in wyniki["suma_kolumn"])
    assert wyniki["suma_przekatnych"]["glowna"] == wyniki["suma_przekatnych"]["przeciwna"]
    assert wyniki["suma_przekatnych"]["glowna"] == wyniki["suma_wierszy"][0]

def test_doubly_even_square():
    kw = magicznyKwadrat(4)
    kw.uzupelnij()
    wyniki = kw.podsumowanie()

    # Sprawdź czy suma wierszy, kolumn i przekątnych jest taka sama
    assert all(s == wyniki["suma_wierszy"][0] for s in wyniki["suma_wierszy"])
    assert all(s == wyniki["suma_kolumn"][0] for s in wyniki["suma_kolumn"])
    assert wyniki["suma_przekatnych"]["glowna"] == wyniki["suma_przekatnych"]["przeciwna"]
    assert wyniki["suma_przekatnych"]["glowna"] == wyniki["suma_wierszy"][0]

def test_singly_even_square():
    kw = magicznyKwadrat(6)
    kw.uzupelnij()
    wyniki = kw.podsumowanie()

    # Sprawdź czy suma wierszy, kolumn i przekątnych jest taka sama
    assert all(s == wyniki["suma_wierszy"][0] for s in wyniki["suma_wierszy"])
    assert all(s == wyniki["suma_kolumn"][0] for s in wyniki["suma_kolumn"])
    assert wyniki["suma_przekatnych"]["glowna"] == wyniki["suma_przekatnych"]["przeciwna"]
    assert wyniki["suma_przekatnych"]["glowna"] == wyniki["suma_wierszy"][0]