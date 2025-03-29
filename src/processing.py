from typing import List, Dict, Union, Any
from datetime import datetime


def filter_by_state(
    transactions: List[Dict[str, Union[str, Any]]],
    state: str = "EXECUTED"
) -> List[Dict[str, Union[str, Any]]]:
    """
    Фильтрует транзакции по состоянию.

    :param transactions: Список словарей с транзакциями.
    :param state: Статус для фильтрации.
    :return: Список транзакций с указанным статусом.
    """
    if transactions is None or not isinstance(transactions, list):
        raise TypeError("Входные данные должны быть списком транзакций.")

    if state is not None and not isinstance(state, str):
        raise TypeError("Состояние должно быть строкой.")

    return [
        transaction for transaction in transactions
        if transaction.get("state") == state
    ]


def sort_by_date(
    data: List[Dict[str, Union[str, Any]]],
    descending: bool = True
) -> List[Dict[str, Union[str, Any]]]:
    """
    Сортирует список словарей по дате.

    :param data: Список словарей, каждый из которых должен содержать ключ 'date'.
    :param descending: Если True, сортировка будет по убыванию, если False — по возрастанию.
    :return: Отсортированный список словарей.
    """
    if data is None or not isinstance(data, list):
        raise TypeError("Input must be a list")

    for item in data:
        if not isinstance(item, dict) or 'date' not in item:
            raise TypeError("Each item must be a dictionary with a 'date' key")

    return sorted(
        data,
        key=lambda x: datetime.fromisoformat(x['date']),
        reverse=descending
    )
