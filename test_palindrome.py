import pytest

from palindrome import insertions_to_make_palindrome


PALINDROME_CASES = [
    ("ab", 1),
    ("abcb", 1),
    ("abcba", 0),
    ("acba", 1),
    ("11223322", 2),
    ("0123456789a", 10),
    ("FFT", 1),
]
@pytest.mark.parametrize("text,insertions", PALINDROME_CASES)
def test_palindrome(text, insertions):
    assert insertions_to_make_palindrome(text) == insertions
