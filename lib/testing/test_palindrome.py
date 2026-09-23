import pytest
from lib.testing.palindrome import longest_palindromic_substring

# --- Basic Cases ---

def test_basic_odd_length_palindrome():
    """Test a standard string where the longest palindrome has an odd length."""
    # "aba" is the longest palindromic substring
    assert longest_palindromic_substring("babad") == "aba" 

def test_basic_even_length_palindrome():
    """Test a standard string where the longest palindrome has an even length."""
    # "bb" is the longest palindromic substring
    assert longest_palindromic_substring("cbbd") == "bb"

def test_entire_string_is_palindrome():
    """Test a string that is entirely a palindrome itself."""
    assert longest_palindromic_substring("racecar") == "racecar"


# --- Edge Cases ---

def test_empty_string():
    """Test that an empty string returns an empty string."""
    assert longest_palindromic_substring("") == ""

def test_single_character():
    """Test that a single character string returns itself."""
    assert longest_palindromic_substring("a") == "a"

def test_no_palindrome_returns_single_char():
    """Test a string with no repeating patterns. 
    Any individual character is a valid palindrome of length 1."""
    result = longest_palindromic_substring("abcde")
    assert len(result) == 1
    assert result in "abcde"

def test_long_string():
    """Test a longer string with a distinct nested palindrome."""
    input_str = "abcdefg" + "tattarrattat" + "hijklmnop"
    assert longest_palindromic_substring(input_str) == "tattarrattat"
