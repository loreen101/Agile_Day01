# test_calculate_sum_of_digits.py
import pytest
from Sum_of_Digits import calculate_sum_of_digits

def test_simple():
    assert calculate_sum_of_digits("a1b2c3") == 6

def test_multiple_digits():
    assert calculate_sum_of_digits("a12b34") == 10  

def test_no_digits():
    assert calculate_sum_of_digits("abcdef") == 0

def test_digits_at_edges():
    assert calculate_sum_of_digits("123abc456") == 21  

def test_empty_string():
    assert calculate_sum_of_digits("") == 0

def test_consecutive_digits():
    assert calculate_sum_of_digits("y1c23c456") == 21  

def test_digits_with_spaces():
    assert calculate_sum_of_digits(" 1 2 3 ") == 6

def test_leading_zeros():
    assert calculate_sum_of_digits("u001v02") == 3  

def test_single_digit():
    assert calculate_sum_of_digits("9") == 9

def test_mixed_characters():
    assert calculate_sum_of_digits("a1b2c3d4e5") == 15