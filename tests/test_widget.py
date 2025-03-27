import pytest
from src.widget import mask_account_card, get_date


# Тесты для функции mask_account_card
@pytest.mark.parametrize(
    "info, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),  # Пример с номером карты
        ("Счет 73654108430135874305", "Счет **4305"),  # Пример с номером счета
        ("MasterCard 1234567812345678", "MasterCard 1234 56** **** 5678"),  # Пример с номером MasterCard
        ("Дебетовая карта 4000123456789010", "Дебетовая карта 4000 12** **** 9010"),  # Пример с номером Visa
    ],
)
def test_mask_account_card(info, expected):
    """Тестирование функции маскировки номера карты или счета."""
    result = mask_account_card(info)
    assert result == expected, f"Expected '{expected}', but got '{result}' for input '{info}'"


# Тесты для некорректного ввода в mask_account_card
@pytest.mark.parametrize(
    "info",
    [
        "",  # Пустая строка
        "Счет 1234",  # Номер счета слишком короткий
        "Некорректный ввод 123",  # Некорректный номер
    ],
)
def test_mask_account_card_invalid(info):
    """Тестирование обработки некорректного ввода в функции маскировки."""
    with pytest.raises(ValueError) as excinfo:
        mask_account_card(info)
    assert "Некорректный ввод" in str(excinfo.value)


# Тесты для функции get_date
@pytest.mark.parametrize(
    "date_str, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),  # Стандартный формат даты
        ("2023-12-31T23:59:59.999999", "31.12.2023"),  # Переход на следующий год
        ("2024-01-01T00:00:00.000000", "01.01.2024"),  # Первый день нового года
    ],
)
def test_get_date(date_str, expected):
    """Тестирование функции преобразования даты из ISO формата."""
    result = get_date(date_str)
    assert result == expected, f"Expected '{expected}', but got '{result}' for input '{date_str}'"


# Тесты для некорректного ввода в get_date
@pytest.mark.parametrize(
    "date_str",
    [
        "invalid-date",  # Некорректный формат даты
        "",  # Пустая строка
    ],
)
def test_get_date_invalid(date_str):
    """Тестирование обработки некорректного формата даты."""
    with pytest.raises(ValueError, match="Некорректный формат даты"):
        get_date(date_str)
