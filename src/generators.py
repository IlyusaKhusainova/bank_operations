def filter_by_currency(transactions, currency_code):
    """
    Фильтрует транзакции по заданной валюте.

    :param transactions: Список словарей с транзакциями.
    :param currency_code: Код валюты для фильтрации.
    :return: Итератор, который возвращает транзакции с заданной валютой.
    """
    for transaction in transactions:
        if transaction['operationAmount']['currency']['code'] == currency_code:
            yield transaction


def transaction_descriptions(transactions):
    """
    Генерирует описания транзакций.

    :param transactions: Список словарей с транзакциями.
    :return: Генератор, который возвращает описания транзакций.
    """
    for transaction in transactions:
        yield transaction['description']


def card_number_generator(start, stop):
    """
    Генерирует номера банковских карт в формате XXXX XXXX XXXX XXXX.

    :param start: Начальное значение для генерации.
    :param stop: Конечное значение для генерации.
    :return: Генератор, который возвращает номера карт.
    """
    for number in range(start, stop + 1):
        yield f"{number:016d}"[:4] + " " + f"{number:016d}"[4:8] + " " + f"{number:016d}"[8:12] + " " + f"{number:016d}"[12:16]