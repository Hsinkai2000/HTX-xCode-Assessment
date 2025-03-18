import re
import string


def filter_phrase(phrase: str) -> str:
    return re.sub(r'[^a-zA-Z0-9]', '', phrase).lower()


def phrase_isPalindrome(phrase: str) -> bool:
    phrase = filter_phrase(phrase)

    n = len(phrase)
    left_pointer, right_pointer = 0, n-1

    while left_pointer < right_pointer:
        if phrase[left_pointer] != phrase[right_pointer]:
            return False
        left_pointer += 1
        right_pointer -= 1

    return True
