import pytest
import import_ipynb
from task1 import verify

# # List of valid card numbers (in different formats)
# valid_card_numbers = [
#     "4539 1488 0343 6467",  # Visa
#     "6011 1111 1111 1117",  # Discover
#     "3714-4963-5398-431",   # AmEx (15 digits)
#     "378282246310005",      # AmEx (no spaces)
#     "30569309025904",       # Diners Club (14 digits)
# ]

# # List of invalid card numbers (wrong check digit, invalid lengths)
# invalid_card_numbers = [
#     "4539 1488 0343 6468",  # Invalid Visa
#     "6011 1111 1111 1118",  # Invalid Discover
#     "3714-4963-5398-432",   # Invalid AmEx
#     "378282246310006",      # Invalid AmEx
#     "30569309025905",       # Invalid Diners Club
#     "1234 5678 9012 3456",  # Random invalid number
#     "1234",                 # Too short
# ]

# @pytest.mark.parametrize("card_number", valid_card_numbers)
# def test_valid_card_numbers(card_number):
#     """
#     Test that valid card numbers return True.
#     """
#     assert verify(card_number) is True

# @pytest.mark.parametrize("card_number", invalid_card_numbers)
# def test_invalid_card_numbers(card_number):
#     """
#     Test that invalid card numbers return False.
#     """
#     assert verify(card_number) is False

# Test valid card numbers with spaces (handled in the function)
@pytest.mark.parametrize("card_number, expected", [
    ("4539 1488 0343 6467", True),
    ("4716 1089 9971 6531", True),
    ("6011 5144 3354 6201", True),
    ("3530 1113 3330 0000", True),
    ("5555 5555 5555 4444", True),
    ("4539 1488 0343 6468", False),  # Invalid Visa
    ("6011 1111 1111 1118", False),  # Invalid Discover
    ("3714-4963-5398-432", False),   # Invalid AmEx
    ("378282246310006", False),      # Invalid AmEx
    ("30569309025905", False),       # Invalid Diners Club
    ("1234 5678 9012 3456", False),  # Random invalid number
    ("1234", False),                 # Too short
], ids=["Visa1", "Visa2", "Discover", "JCB", "Mastercard",
        "Invalid_Visa", "Invalid_Discover", "Invalid_AmEx", "Invalid_AmEx", "Invalid_Diners_Club",
        "Random_invalid_number", "Too_short"])
def test_valid_card_numbers(card_number, expected):
    assert verify(card_number) == expected


