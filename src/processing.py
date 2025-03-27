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
    print(f"Sorting transactions: {transactions}")  # Отладочное сообщение
    if not isinstance(transactions, list):
        raise TypeError("Входные данные должны быть списком транзакций.")

    sorted_transactions = sorted(transactions, key=lambda x: x["date"], reverse=descending)
    print(f"Sorted transactions: {sorted_transactions}")  # Отладочное сообщение
    return sorted_transactions