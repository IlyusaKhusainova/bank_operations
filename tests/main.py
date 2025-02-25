# test_masks.py

from src.masks import get_mask_card_number, get_mask_account
from src.widget import mask_account_card, get_date

def test_get_mask_card_number():
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"

def test_get_mask_account():
    assert get_mask_account("73654108430135874305") == "**4305"

def test_mask_account_card():
    assert mask_account_card("Visa Platinum 7000792289606361") == "Visa Platinum 7000 79** **** 6361"
    assert mask_account_card("Счет 73654108430135874305") == "Счет **4305"

def test_get_date():
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"