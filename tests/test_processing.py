import pytest
from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def sample_data():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2021-06-01T02:26:18"},
        {"id": 2, "state": "CANCELED", "date": "2021-07-01T02:26:18"},
        {"id": 3, "state": "EXECUTED", "date": "2021-06-02T02:26:18"},
    ]


def test_filter_by_state(sample_data):
    # Проверка фильтрации по умолчанию (EXECUTED)
    assert filter_by_state(sample_data) == [
        {"id": 1, "state": "EXECUTED", "date": "2021-06-01T02:26:18"},
        {"id": 3, "state": "EXECUTED", "date": "2021-06-02T02:26:18"},
    ]
    # Проверка фильтрации по состоянию CANCELED
    assert filter_by_state(sample_data, "CANCELED") == [
        {"id": 2, "state": "CANCELED", "date": "2021-07-01T02:26:18"},
    ]
    # Проверка фильтрации по несуществующему состоянию
    assert filter_by_state(sample_data, "NON_EXISTENT") == []


def test_filter_by_state_invalid():
    # Проверка на None
    with pytest.raises(TypeError):
        filter_by_state(None)
    # Проверка на некорректный тип
    with pytest.raises(TypeError):
        filter_by_state("not a list")


@pytest.mark.parametrize(
    "data,expected",
    [
        (
            [{"id": 1, "date": "2021-06-02T02:26:18"}, {"id": 2, "date": "2021-05-01T02:26:18"}],
            [{"id": 2, "date": "2021-05-01T02:26:18"}, {"id": 1, "date": "2021-06-02T02:26:18"}],
        ),
        (
            [{"id": 1, "date": "2021-01-01T02:26:18"}, {"id": 2, "date": "2021-01-02T02:26:18"}],
            [{"id": 1, "date": "2021-01-01T02:26:18"}, {"id": 2, "date": "2021-01-02T02:26:18"}],
        ),
    ],
)
def test_sort_by_date(data, expected):
    sorted_data = sort_by_date(data, descending=False)  # Сортируем по возрастанию
    assert sorted_data == expected, f"Ожидалось {expected}, но получено {sorted_data} для входных данных {data}"


@pytest.fixture
def transaction_data():
    return [
        {"id": 1, "date": "2023-10-01T02:26:18"},
        {"id": 2, "date": "2023-09-15T02:26:18"},
        {"id": 3, "date": "2023-10-05T02:26:18"},
        {"id": 4, "date": "2023-08-20T02:26:18"},
    ]


def test_sort_by_date_descending(transaction_data):
    sorted_transactions = sort_by_date(transaction_data)
    assert sorted_transactions[0]["id"] == 3  # Latest date
    assert sorted_transactions[1]["id"] == 1
    assert sorted_transactions[2]["id"] == 2
    assert sorted_transactions[3]["id"] == 4  # Oldest date


def test_sort_by_date_ascending(transaction_data):
    sorted_transactions = sort_by_date(transaction_data, descending=False)
    assert sorted_transactions[0]["id"] == 4  # Oldest date
    assert sorted_transactions[1]["id"] == 2
    assert sorted_transactions[2]["id"] == 1
    assert sorted_transactions[3]["id"] == 3  # Latest date


def test_sort_by_date_empty():
    sorted_transactions = sort_by_date([])
    assert sorted_transactions == []


def test_sort_by_date_invalid_input():
    # Проверка на None
    with pytest.raises(TypeError):
        sort_by_date(None)

    # Проверка на некорректный тип (строка)
    with pytest.raises(TypeError):
        sort_by_date("not a list")

    # Проверка на некорректный тип (число)
    with pytest.raises(TypeError):
        sort_by_date(123)

    # Проверка на некорректный тип (словарь)
    with pytest.raises(TypeError):
        sort_by_date({"id": 1, "date": "2021-01-01T02:26:18"})


def test_sort_by_date_mixed_formats():
    data = [
        {"id": 1, "date": "2021-06-02T02:26:18"},
        {"id": 2, "date": "2021-05-01"},
        {"id": 3, "date": "2021-06-01T02:26:18"},
    ]
    expected = [
        {"id": 2, "date": "2021-05-01"},
        {"id": 3, "date": "2021-06-01T02:26:18"},
        {"id": 1, "date": "2021-06-02T02:26:18"},
    ]
    sorted_data = sort_by_date(data, descending=False)
    assert sorted_data == expected


def test_sort_by_date_same_date():
    data = [
        {"id": 1, "date": "2021-06-01T02:26:18"},
        {"id": 2, "date": "2021-06-01T02:26:18"},
        {"id": 3, "date": "2021-06-01T02:26:18"},
    ]
    expected = [
        {"id": 1, "date": "2021-06-01T02:26:18"},
        {"id": 2, "date": "2021-06-01T02:26:18"},
        {"id": 3, "date": "2021-06-01T02:26:18"},
    ]
    sorted_data = sort_by_date(data, descending=False)
    assert sorted_data == expected