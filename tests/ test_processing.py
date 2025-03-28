import pytest
from processing import filter_by_state, sort_by_date


@pytest.fixture
def sample_data():
    # Возвращает образец данных для тестирования
    return [
        {'id': 1, 'state': 'EXECUTED', 'date': '2021-06-01T02:26:18'},
        {'id': 2, 'state': 'CANCELED', 'date': '2021-07-01T02:26:18'},
        {'id': 3, 'state': 'EXECUTED', 'date': '2021-06-02T02:26:18'},
    ]


def test_filter_by_state(sample_data):
    # Тестирование фильтрации по состоянию без параметра
    assert filter_by_state(sample_data) == [
        {'id': 1, 'state': 'EXECUTED', 'date': '2021-06-01T02:26:18'},
        {'id': 3, 'state': 'EXECUTED', 'date': '2021-06-02T02:26:18'},
    ]
    # Тестирование фильтрации по конкретному состоянию
    assert filter_by_state(sample_data, 'CANCELED') == [
        {'id': 2, 'state': 'CANCELED', 'date': '2021-07-01T02:26:18'},
    ]
    # Тестирование фильтрации по несуществующему состоянию
    assert filter_by_state(sample_data, 'NON_EXISTENT') == []


@pytest.mark.parametrize("data,expected", [
    ([
        {'id': 1, 'date': '2021-06-02T02:26:18'},
        {'id': 2, 'date': '2021-05-01T02:26:18'}
    ],
     [
        {'id': 2, 'date': '2021-05-01T02:26:18'},
        {'id': 1, 'date': '2021-06-02T02:26:18'}
     ]),
    ([
        {'id': 1, 'date': '2021-01-01T02:26:18'},
        {'id': 2, 'date': '2021-01-02T02:26:18'}
    ],
     [
        {'id': 1, 'date': '2021-01-01T02:26:18'},
        {'id': 2, 'date': '2021-01-02T02:26:18'}
     ]),
])
def test_sort_by_date(data, expected):
    # Проверка, что сортировка по дате работает корректно
    sorted_data = sort_by_date(data)
    assert sorted_data == expected, f"Expected {expected}, but got {sorted_data} for input {data}"
