import pytest
from src.phrase_isPalindrome import phrase_isPalindrome, filter_phrase


def test_phrase_with_spaces_and_mixed_case_is_palindrome():
    assert filter_phrase(
        "Was it a car or a cat I saw?") == "wasitacaroracatisaw"
    assert phrase_isPalindrome("Was it a car or a cat I saw?") is True


def test_phrase_with_spaces_is_not_palindrome():
    assert filter_phrase("Hello World") == "helloworld"
    assert phrase_isPalindrome("Hello World") is False


def test_phrase_with_only_special_chars_is_empty_and_palindrome():
    assert filter_phrase("!?") == ""
    assert phrase_isPalindrome("!?") is True


def test_phrase_with_special_chars_in_middle_is_palindrome():
    assert filter_phrase(
        "Was it !a car, or a. cat I saw?") == "wasitacaroracatisaw"
    assert phrase_isPalindrome("Was it !a car, or a. cat I saw?") is True


def test_camel_case_phrase_is_palindrome():
    assert filter_phrase("WasItACarOrACatISaw") == "wasitacaroracatisaw"
    assert phrase_isPalindrome("WasItACarOrACatISaw?") is True


def test_empty_phrase_is_palindrome():
    assert filter_phrase("") == ""
    assert phrase_isPalindrome("") is True
