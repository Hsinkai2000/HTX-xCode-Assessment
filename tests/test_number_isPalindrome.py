import pytest
from src.number_isPalindrome import number_isPalindrome


def test_valid_palindrome():
    assert number_isPalindrome(121) is True


def test_zero_is_palindrome():
    assert number_isPalindrome(0) is True


def test_negative_not_palindrome():
    assert number_isPalindrome(-121) is False


def test_multiple_of_ten_not_palindrome():
    assert number_isPalindrome(10) is False


def test_single_digit_valid_palindrome():
    assert number_isPalindrome(5) is True
    assert number_isPalindrome(8) is True


def test_large_numbers():
    assert number_isPalindrome(2147483647) is False


def test_odd_len():
    assert number_isPalindrome(999333999) is True
    assert number_isPalindrome(999336999) is False


def test_even_len():
    assert number_isPalindrome(992299) is True
    assert number_isPalindrome(982299) is False
