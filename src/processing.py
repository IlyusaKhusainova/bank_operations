from typing import List, Dict

def filter_by_state(transactions: List[Dict], state: str = "EXECUTED") -> List[Dict]:
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

    return [transaction for transaction in transactions if transaction.get("state") == state]


def sort_by_date(transactions: List[Dict], descending: bool = True) -> List[Dict]:
    """
    Сортирует транзакции по дате.

    :param transactions: Список словарей с транзакциями.
    :param descending: Указывает, по убыванию ли сортировать.
    :return: Отсортированный список транзакций.
    """
    if not isinstance(transactions, list):
        raise TypeError("Входные данные должны быть списком транзакций.")

    return sorted(transactions, key=lambda x: x["date"], reverse=descending)