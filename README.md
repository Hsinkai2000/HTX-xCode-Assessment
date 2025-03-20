# HTX xCode Technical Assessment

## Table of Contents

- [Overview](#overview)
- [Repository Structure](#repository-structure)
- [Setup Instructions](#setup-instructions)
- [Tests and Coverage](#tests-and-coverage)
- [Implementation Details](#implementation-details)

---

## Overview

This repository contains my submission for the HTX xCode Technical Test (2025) for the Backend Engineer role. The implementation follows clean code principles, efficient algorithms, and best practices in version control and software design.

---

## Repository Structure

```
 ├── src
 │ ├── __init__.py
 │ ├── number_isPalindrome.py # Function to test for number is palindrome
 │ ├── phrase_isPalindrome.py # Function to test for phrase is palindrome
 ├── tests
 │ ├── __init__.py
 │ ├── test_number_isPalindrome.py # Unit tests to test for number is palindrome
 │ ├── test_phrase_isPalindrome.py # Unit tests to test for phrase is palindrome
 ├── .gitignore
 ├── README.md # Documentation
 ├── requirements.txt # requirements of python files
```

---

## Setup Instructions

### Pre-requisites

Ensure you have the following installed:

- Python 3.8+
- Git

### Clone the repository

```sh
git clone https://github.com/Hsinkai2000/HTX-xCode-Assessment.git
cd HTX-xCode-Assessment
```

### Installing Dependencies

```sh
pip install -r requirements.txt
```

---

## Tests and Coverage

To run tests and check coverage, run the following command:

```sh
pytest --cov=src --cov-report=term-missing
```

This should provide you with an overview and coverage of the test cases.

For a more in-depth view of what unit tests are conducted, run:

```sh
pytest -v tests
```

---

## Implementation Details

### Design Patterns Used

- Two-pointer technique for phrase palindrome checking.
- Mathematical approach using modulo and floor division for number palindrome checking

---

### Question 1: Phrase is Palindrome

**Function:** `phrase_isPalindrome(phrase: str) -> bool`
**Approach:**

- Remove non-alphanumeric characters via REGEX.
- Convert phrase to lowercase.
- Use two pointer technique to check if phrase is palindrome. Break out once detect pointers differ in value.

**Time Complexity:** O(n), Only iterates through the filter once and the phrase another time to find result in O(2n) time, where **n** is the length of phrase.

**Space Complexity:** O(1), uses the same input string without creating new phrases.

---

### Question 2: Number is Palindrome

**Function:** `number_isPalindrome(number: str) -> bool`
**Approach:**

- Handle negative cases and multiple of tens excluding 0 as they will never be a palindrome.
- Traverse the input number backwards by getting remainder and remove final digit from input number by floor division.
- Repeat until forward value is smaller than backward value.
- Check if any of following is true:
  - Odd length: forward value = backward value floor divided by 10
  - Even length: forward value = backward value

**Time Complexity:** O(log n), processing the input digit by digit, dividing by 10, the number of iterations in the loop is proportional to the number of digits, where **n** is input number.

**Space Complexity:** O(1), uses a few integer variables to track with no additional data structures.

---

### Unit Tests

Unit Tests are written using pytest with coverage as a key metric.

**Test cases covered:**

- Phrase is Palindrome:
  - Regular palindrome phrases
  - Non-palindromic phrases
  - Special characters
  - Mixed cases and punctuation
  - Empty string case
- Number is Palindrome
  - Valid Palindromic numbers
  - Zero as a palindrome
  - Negative numbers
  - Multiples of tens
  - Single digit numbers as palindromes
  - large numbers
  - Odd-length palindromes
  - Even-length palindromes

Total Tests: 14
Total Passed: 14
Coverage: 100%

---

### Version Control Best Practices

- Used `.gitignore` to exclude unnecessary files
- Commit messages follows conventional commit guidelines
- Organised folders according to github best practice guidelines

---
