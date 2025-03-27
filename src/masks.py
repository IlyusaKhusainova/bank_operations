def get_mask_card_number(card_number: str) -> str:
    """Возвращает замаскированный номер карты, оставляя только последние 4 цифры видимыми."""
    if not card_number or len(card_number) < 4 or not card_number.isdigit():
        raise ValueError("Некорректный номер карты")
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"

def get_mask_account(account_number: str) -> str:
    """Возвращает замаскированный номер счета, оставляя только последние 4 цифры видимыми."""
    if not account_number or len(account_number) < 4 or not account_number.isdigit():
        raise ValueError("Некорректный номер счета")
    return f"**{account_number[-4:]}"