def get_mask_card_number(card_number):
    """Маскирует все, кроме первых 4 и последних 4 цифр номера карты."""
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number):
    """Маскирует все, кроме последних 4 цифр номера счета."""
    return f"**{account_number[-4:]}"


def mask_account_card(account_card):
    """Разделяет строку с номером карты и маскирует номер карты или номер счета соответственно."""
    parts = account_card.split()
    if len(parts) > 1:
        # Предполагаем, что последняя часть - это номер карты или номер счета
        masked_part = get_mask_card_number(parts[-1]) if len(parts[-1]) == 16 else get_mask_account(parts[-1])
        return ' '.join(parts[:-1] + [masked_part])
    return account_card


def get_date(date_string):
    """Преобразует строку даты в желаемый формат."""
    from datetime import datetime
    dt = datetime.fromisoformat(date_string)
    return dt.strftime("%d.%m.%Y")


if __name__ == "__main__":
    get_mask_card_number()
    get_mask_account()
    mask_account_card()
    get_date()
