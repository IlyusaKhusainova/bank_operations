import pytest
from masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize("card_number,expected", [
    ("7000792289606361", "7000 79** **** 6361"),  # стандартный номер карты
    ("1234567890123456", "1234 56** **** 3456"),  # другой номер карты
    ("", None),  # отсутствующий номер
    ("9999123456781234", "9999 12** **** 1234"),  # номер карты с другим форматом
    ("4111111111111111", "4111 11** **** 1111"),  # номер Visa
])
def test_get_mask_card_number(card_number, expected):
    result = get_mask_card_number(card_number)
    assert result == expected, f"Expected {expected}, but got {result} for input '{card_number}'"


@pytest.mark.parametrize("account_number,expected", [
    ("73654108430135874305", "**4305"),  # стандартный номер счета
    ("123456", None),  # слишком короткий номер
    ("", None),  # отсутствующий номер
    ("12345678901234567890", "**7890"),  # стандартный номер долгого счета
    ("9876543214321", "**4321"),  # номер счёта с другим форматом
])
def test_get_mask_account(account_number, expected):
    result = get_mask_account(account_number)
    assert result == expected, f"Expected {expected}, but got {result} for input '{account_number}'"


