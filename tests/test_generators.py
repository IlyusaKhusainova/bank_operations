import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator
from typing import List, Dict, Any


@pytest.fixture
def transactions() -> List[Dict[str, Any]]:
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        }
    ]


def test_filter_by_currency(transactions: List[Dict[str, Any]]) -> None:
    # Тестирование фильтрации по USD
    usd_transactions = list(filter_by_currency(transactions, "USD"))
    assert len(usd_transactions) == 2
    assert all(tx['operationAmount']['currency']['code'] == "USD" for tx in usd_transactions)

    # Тестирование фильтрации по RUB
    rub_transactions = list(filter_by_currency(transactions, "RUB"))
    assert len(rub_transactions) == 1
    assert all(tx['operationAmount']['currency']['code'] == "RUB" for tx in rub_transactions)

    # Тестирование фильтрации по несуществующей валюте
    nonexistent_transactions = list(filter_by_currency(transactions, "EUR"))
    assert len(nonexistent_transactions) == 0

    # Тестирование фильтрации на пустом списке
    empty_transactions: List[Dict[str, Any]] = []
    empty_result = list(filter_by_currency(empty_transactions, "USD"))
    assert len(empty_result) == 0


def test_transaction_descriptions(transactions: List[Dict[str, Any]]) -> None:
    # Проверка, что функция возвращает корректные описания
    descriptions = list(transaction_descriptions(transactions))
    assert descriptions == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет"
    ]

    # Проверка на пустом списке
    empty_descriptions = list(transaction_descriptions([]))
    assert empty_descriptions == []


def test_card_number_generator() -> None:
    # Проверка генерации номеров карт в заданном диапазоне
    generated_numbers: List[str] = list(card_number_generator(1, 5))
    assert generated_numbers == [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005"
    ]

    # Проверка генерации с одним номером
    single_number: List[str] = list(card_number_generator(1, 1))
    assert single_number == ["0000 0000 0000 0001"]

    # Проверка генерации с диапазоном, где start > stop
    reverse_range: List[str] = list(card_number_generator(5, 1))
    assert reverse_range == []

    # Проверка генерации с нулевым диапазоном
    zero_range: List[str] = list(card_number_generator(0, 0))
    assert zero_range == ["0000 0000 0000 0000"]