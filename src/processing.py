from typing import List, Dict


def filter_by_state(transactions: List[Dict], state: str = 'EXECUTED') -> List[Dict]:
    """
    Фильтрует транзакции по состоянию.

    :param transactions: Список словарей с транзакциями.
    :param state: Статус для фильтрации.
    :return: Список транзакций с указанным статусом.
    """
    return [transaction for transaction in transactions if transaction.get('state') == state]


from typing import List, Dict


def sort_by_date(transactions: List[Dict], descending: bool = True) -> List[Dict]:
    """
    Сортирует транзакции по дате.

    :param transactions: Список словарей с транзакциями.
    :param descending: Указывает, по убыванию ли сортировать.
    :return: Отсортированный список транзакций.
    """
    return sorted(transactions, key=lambda x: x['date'], reverse=descending)

if __name__ == "__main__":
    sample_data = [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]

    print(filter_by_state(sample_data))
    print(filter_by_state(sample_data, 'CANCELED'))
    print(sort_by_date(sample_data))