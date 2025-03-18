def number_isPalindrome(number: int) -> bool:
    """
        This function takes an integer and returns a boolean checking if input integer is a palindrome 
    """
    if number < 0 or (number % 10 == 0 and number != 0):
        return False

    back_traversed = 0
    while number > back_traversed:
        back_traversed *= 10
        back_traversed += number % 10
        number //= 10

    return number == back_traversed//10 or number == back_traversed
