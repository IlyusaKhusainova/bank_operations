from typing import List, Dict, Any, Generator


def filter_by_currency(
    transactions: List[Dict[str, Any]], currency_code: str
) -> Generator[Dict[str, Any], None, None]:
    """
    Фильтрует транзакции по заданной валюте.

    :param transactions: Список словарей с транзакциями.
    :param currency_code: Код валюты для фильтрации.
    :return: Итератор, который возвращает транзакции с заданной валютой.
    """
    for transaction in transactions:
        if transaction['operationAmount']['currency']['code'] == currency_code:
            yield transaction


def transaction_descriptions(
    transactions: List[Dict[str, Any]]
) -> Generator[str, None, None]:
    """
    Генерирует описания транзакций.

    :param transactions: Список словарей с транзакциями.
    :return: Генератор, который возвращает описания транзакций.
    """
    for transaction in transactions:
        yield transaction['description']


def card_number_generator(start: int, stop: int) -> Generator[str, None, None]:
    """
    Генерирует номера банковских карт в формате XXXX XXXX XXXX XXXX.

    :param start: Начальное значение для генерации.
    :param stop: Конечное значение для генерации.
    :return: Генератор, который возвращает номера карт.
    """
    for number in range(start, stop + 1):
        formatted_number = f"{number:016d}"
        yield (
            f"{formatted_number[:4]} {formatted_number[4:8]} "
            f"{formatted_number[8:12]} {formatted_number[12:16]}"
        )
