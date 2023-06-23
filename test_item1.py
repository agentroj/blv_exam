import pytest
from item1 import caesar_cipher


# Pytest scenarios
def test_caesar_cipher_positive_shift():
    assert caesar_cipher("AbCdE", 5) == "FgHiJ"


def test_caesar_cipher_negative_shift():
    assert caesar_cipher("AbCdE", -5) == "VwXyZ"


def test_caesar_cipher_direct_substitution():
    encoding_dict = {"A": "X", "C": "T", "E": "F"}
    assert caesar_cipher("AbCdE", encoding_dict) == "XbTdF"


def test_caesar_cipher_non_letter_characters():
    assert caesar_cipher("Hello, World!", 3) == "Khoor, Zruog!"


def test_caesar_cipher_mixed_case():
    assert caesar_cipher("AbCdEfG", -2) == "YzAbCdE"


def test_caesar_cipher_invalid_encoding_key():
    with pytest.raises(ValueError):
        caesar_cipher("AbCdE", 2.5)


def test_caesar_cipher_empty_string():
    assert caesar_cipher("", 1) == ""


# Run pytest
pytest.main()
