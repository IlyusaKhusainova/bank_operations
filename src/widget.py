from datetime import datetime
from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(input_string: str) -> str:
    """Маскировка номера карты или счета на основе входящего типа."""
    if not input_string or len(input_string.split()) < 2:
        raise ValueError("Некорректный ввод")

    parts = input_string.split()
    account_type = " ".join(parts[:-1])  # Все, кроме последнего элемента
    account_number = parts[-1]

    # Проверка на минимальную длину номера счета или карты
    if len(account_number) < 10 or not account_number.isdigit():
        raise ValueError("Некорректный ввод")

    if "счет" in account_type.lower():
        masked_account = get_mask_account(account_number)
        return f"{account_type} {masked_account}"
    else:
        masked_card = get_mask_card_number(account_number)
        return f"{account_type} {masked_card}"


def get_date(date_string: str) -> str:
    """Преобразует дату из формата ISO в формат ДД.ММ.ГГГГ."""
    # Проверка на пустую строку
    if not date_string:
        raise ValueError("Некорректный формат даты")

    try:
        # Преобразование строки в объект datetime
        date_time = datetime.fromisoformat(date_string)
    except ValueError:
        raise ValueError("Некорректный формат даты")

    # Форматирование даты в нужный формат
    return date_time.strftime("%d.%m.%Y")
