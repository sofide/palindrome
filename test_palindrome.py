import pytest

from palindrome import insertions_to_palindrome


PALINDROME_CASES = [
    ("ab", 1),
    ("abcb", 1),
    ("abcba", 0),
    ("acba", 1),
    ("11223322", 2),
    ("0123456789a", 10),
    ("FFT", 1),
    ("1235676541", 3),  # missing 4 from the left and 3 and 2 from the right
]
@pytest.mark.parametrize("text,insertions", PALINDROME_CASES)
def test_palindrome(text, insertions):
    assert insertions_to_palindrome(text) == insertions
