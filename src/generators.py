from typing import List, Dict, Any, Generator


def filter_by_currency(transactions: List[Dict[str, Any]], currency_code: str) -> List[Dict[str, Any]]:
    """Фильтрует транзакции по заданной валюте."""
    return [
        transaction for transaction in transactions
        if transaction.get('operationAmount', {}).get('currency', {}).get('code') == currency_code
    ]


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Generator[str, None, None]:
    """Генерирует описания транзакций."""
    for transaction in transactions:
        description = transaction.get('description')
        if description is None:
            yield 'Описание отсутствует'
        else:
            yield description


def card_number_generator(transactions: List[Dict[str, Any]]) -> Generator[str, None, None]:
    """Генерирует номера карт из транзакций."""
    for transaction in transactions:
        from_field = transaction.get('from', '')
        if from_field:  # Проверяем, что поле 'from' не пустое
            card_number = from_field.split()[-1]  # Получаем последнюю часть
            yield f'**** **** **** {card_number[-4:]}'  # Маскируем все, кроме последних 4 цифр
