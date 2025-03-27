import pytest
from widget import mask_account_card, get_date


@pytest.mark.parametrize("info,expected", [
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),  # Стандартный пример с номером карты
    ("Счет 73654108430135874305", "Счет **4305"),  # Стандартный пример с номером счета
    ("MasterCard 1234567812345678", "MasterCard 1234 56** **** 5678"),  # Пример с номером MasterCard
    ("Дебетовая карта 4000123456789010", "Дебетовая карта 4000 12** **** 9010"),  # Пример с номером Visa
    ("", None),  # Пустая строка
    ("Счет 1234", None),  # Номер счета слишком короткий
])
def test_mask_account_card(info, expected):
    result = mask_account_card(info)
    assert result == expected, f"Expected {expected}, but got {result} for input '{info}'"


@pytest.mark.parametrize("date_str,expected", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),  # Стандартный формат даты
    ("invalid-date", None),  # Некорректный формат даты
    ("2023-12-31T23:59:59.999999", "31.12.2023"),  # Переход на следующий год
    ("2024-01-01T00:00:00.000000", "01.01.2024"),  # Первый день нового года
    ("", None),  # Пустая строка
])
def test_get_date(date_str, expected):
    result = get_date(date_str)
    assert result == expected, f"Expected {expected}, but got {result} for input '{date_str}'"
