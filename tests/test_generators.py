import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


@pytest.fixture
def transactions():
    return [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2023-01-01T10:00:00.000Z",
            "operationAmount": {
                "amount": "1000.00",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 12345678901234567890",
            "to": "Счет 09876543210987654321"
        },
        {
            "id": 2,
            "state": "EXECUTED",
            "date": "2023-01-02T10:00:00.000Z",
            "operationAmount": {
                'amount': '2000.00',
                'currency': {
                    'name': 'EUR',
                    'code': 'EUR'
                }
            },
            'description': None,
        },
        {
            'id': 3,
            'state': 'EXECUTED',
            'date': '2023-01-03T10:00:00.000Z',
            'operationAmount': {
                'amount': '1500.00',
                'currency': {
                    'name': 'RUB',
                    'code': 'RUB'
                }
            },
            'description': 'Перевод организации',
        },
        {
            'id': 4,
            'state': 'EXECUTED',
            'date': '2023-01-04T10:00:00.000Z',
        }
    ]


def test_filter_by_currency(transactions):
    usd_transactions = list(filter_by_currency(transactions, 'USD'))
    assert len(usd_transactions) == 1
    assert usd_transactions[0]['id'] == 1

    eur_transactions = list(filter_by_currency(transactions, 'EUR'))
    assert len(eur_transactions) == 1
    assert eur_transactions[0]['id'] == 2

    rub_transactions = list(filter_by_currency(transactions, 'RUB'))
    assert len(rub_transactions) == 1
    assert rub_transactions[0]['id'] == 3

    gbp_transactions = list(filter_by_currency(transactions, 'GBP'))
    assert len(gbp_transactions) == 0


def test_filter_by_currency_with_missing_keys(transactions):
    filtered_transactions = list(filter_by_currency(transactions, 'RUB'))
    assert len(filtered_transactions) == 1
    assert filtered_transactions[0]['id'] == 3


def test_transaction_descriptions(transactions):
    descriptions = list(transaction_descriptions(transactions))
    assert len(descriptions) == len(transactions)

    assert descriptions[0] == 'Перевод организации'
    assert descriptions[1] == 'Описание отсутствует'
    assert descriptions[2] == 'Перевод организации'
    assert descriptions[3] == 'Описание отсутствует'


def test_transaction_descriptions_with_missing_keys(transactions):
    missing_description_transaction = {'id': 5}
    transactions.append(missing_description_transaction)

    descriptions = list(transaction_descriptions(transactions))
    assert descriptions[-1] == 'Описание отсутствует'


def test_card_number_generator(transactions):
    card_numbers = list(card_number_generator(transactions))
    assert len(card_numbers) == 1
    assert card_numbers[0] == '**** **** **** 7890'


def test_card_number_generator_with_missing_keys():
    transactions_with_missing_keys = [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2023-01-01T10:00:00.000Z",
            "operationAmount": {
                "amount": "1000.00",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
        },
        {
            "id": 2,
            "state": "EXECUTED",
            "date": "2023-01-02T10:00:00.000Z",
            "operationAmount": {
                "amount": "2000.00",
                "currency": {
                    "name": "EUR",
                    "code": "EUR"
                }
            },
            "from": "Счет 9876543210123456",
        }
    ]

    card_numbers = list(card_number_generator(transactions_with_missing_keys))
    assert len(card_numbers) == 1
    assert card_numbers[0] == '**** **** **** 3456'


def test_card_number_generator_with_empty_from_field():
    transactions_with_empty_from = [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2023-01-01T10:00:00.000Z",
            "operationAmount": {
                "amount": "1000.00",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "from": "",  # Пустое поле from
        }
    ]

    card_numbers = list(card_number_generator(transactions_with_empty_from))
    assert len(card_numbers) == 0  # Это должно пройти
