import pytest
from src.masks import get_mask_card_number, get_mask_account
from typing import Optional


# Тестирование функции get_mask_card_number
@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("1234567890123456", "1234 56** **** 3456"),
        ("9999123456781234", "9999 12** **** 1234"),
        ("4111111111111111", "4111 11** **** 1111"),
    ],
)
def test_get_mask_card_number(card_number: str, expected: str) -> None:
    result: str = get_mask_card_number(card_number)
    assert result == expected, f"Expected {expected}, but got {result} for input '{card_number}'"


# Тестирование функции get_mask_account
@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("73654108430135874305", "**4305"),
        ("123456", "**3456"),  # Ожидаем замаскированный номер
        ("12345678901234567890", "**7890"),
        ("9876543214321", "**4321"),
    ],
)
def test_get_mask_account(account_number: str, expected: str) -> None:
    result: str = get_mask_account(account_number)
    assert result == expected, f"Expected {expected}, but got {result} for input '{account_number}'"


# Тестирование некорректных номеров карт
@pytest.mark.parametrize(
    "invalid_card_number",
    [
        "",  # Пустая строка
        "abc1234567890123",  # Некорректный формат
        None,  # None
    ],
)
def test_get_mask_card_number_invalid(invalid_card_number: Optional[str]) -> None:
    with pytest.raises(ValueError):
        get_mask_card_number(invalid_card_number)  # Ожидаем ValueError для некорректного ввода


# Тестирование некорректных номеров счетов
@pytest.mark.parametrize(
    "invalid_account_number",
    [
        "",  # Пустая строка
        "abc123",  # Некорректный формат
        None,  # None
    ],
)
def test_get_mask_account_invalid(invalid_account_number: Optional[str]) -> None:
    with pytest.raises(ValueError):
        get_mask_account(invalid_account_number)  # Ожидаем ValueError для некорректного ввода
