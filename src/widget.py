from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(input_string: str) -> str:
    """Маскировка номера карты или счета на основе входящего типа."""
    parts = input_string.split()
    account_type = parts[0]
    account_number = parts[-1]

    if "счет" in account_type.lower():
        masked_account = get_mask_account(account_number)
        return f"{account_type} {masked_account}"
    else:
        masked_card = get_mask_card_number(account_number)
        return f"{account_type} {masked_card}"


def get_date(date_string: str) -> str:
    """Преобразует дату из формата ISO в формат ДД.ММ.ГГГГ."""
    date_time = datetime.fromisoformat(date_string)
    return date_time.strftime("%d.%m.%Y")
