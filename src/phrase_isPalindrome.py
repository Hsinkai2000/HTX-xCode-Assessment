import re
import string


def filter_phrase(phrase: str) -> str:
    """
        This function takes a string and returns the string with only lowercased alphanumerics characters.
    """
    return re.sub(r'[^a-zA-Z0-9]', '', phrase).lower()


def phrase_isPalindrome(phrase: str) -> bool:
    """
        This function takes a string and returns a boolean checking if input string is a palindrome 
    """
    phrase = filter_phrase(phrase)

    n = len(phrase)
    left_pointer, right_pointer = 0, n-1

    while left_pointer < right_pointer:
        if phrase[left_pointer] != phrase[right_pointer]:
            return False
        left_pointer += 1
        right_pointer -= 1

    return True
