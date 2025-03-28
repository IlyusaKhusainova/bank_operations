def get_mask_card_number(card_number):
    """Маскирует все, кроме первых 4 и последних 4 цифр номера карты."""
    if len(card_number) == 16 and card_number.isdigit():
        return f"{card_number[:4]} ** **** {card_number[-4:]}"
    raise ValueError("Номер карты должен содержать 16 цифр и состоять только из цифр.")


def get_mask_account(account_number):
    """Маскирует все, кроме последних 4 цифр номера счета."""
    if account_number.isdigit() and len(account_number) >= 4:
        masked_part = "*" * (len(account_number) - 4)
        return f"{masked_part}{account_number[-4:]}"
    raise ValueError("Номер счета должен содержать как минимум 4 цифры и состоять только из цифр.")


def mask_account_card(account_card):
    """Разделяет строку с номером карты и маскирует номер карты или номер счета соответственно."""
    parts = account_card.split()
    if len(parts) < 2:
        raise ValueError("Необходимо указать имя и номер карты или счета.")

    last_part = parts[-1]
    if len(last_part) == 16 and last_part.isdigit():
        masked_part = get_mask_card_number(last_part)
    elif len(last_part) >= 4 and last_part.isdigit():
        masked_part = get_mask_account(last_part)
    else:
        raise ValueError("Некорректный номер карты или счета.")

    return " ".join(parts[:-1] + [masked_part])


def get_date(date_string):
    """Преобразует строку даты в желаемый формат."""
    from datetime import datetime

    try:
        # Предполагается, что входная строка будет в формате YYYY-MM-DD
        dt = datetime.strptime(date_string, "%Y-%m-%d")
        return dt.strftime("%d.%m.%Y")  # Возвращаем формат DD.MM.YYYY
    except ValueError:
        raise ValueError("Недопустимый формат даты. Ожидаемый формат: YYYY-MM-DD")


if __name__ == "__main__":
    print(get_mask_card_number("1234567812345678"))  # 1234 ** **** 5678
    print(get_mask_account("1234567890123456"))  # ********3456
    print(mask_account_card("User  Name 1234567812345678"))  # User Name 1234 ** **** 5678
    print(get_date("2023-10-10"))  # 10.10.2023
