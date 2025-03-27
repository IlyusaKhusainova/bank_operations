# bank_operations

## Описание 
     Это проект для обработки банковских операций, включая функции фильтрации и сортировки транзакций.

     ## Установка
     Для работы с проектом вам нужно:
     1. Клонировать репозиторий:
bash
        git clone https://github.com/username/bank_operations.git

    2. Установить зависимости (если используются):
bash
        pip install -r requirements.txt
## Использование

     ### Функция filter_by_state

python
     from src.processing import filter_by_state
     transactions = [
         {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
         {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}
     ]
     executed_transactions = filter_by_state(transactions)

     ### Функция sort_by_date

python
     from src.processing import sort_by_date
     sorted_transactions = sort_by_date(transactions)

## Примеры
     - Выход функции filter_by_state() со статусом по умолчанию 'EXECUTED':
python
     [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]

    - Выход функции 
sort_by_date()
 (по убыванию):
python
     [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, ...]
