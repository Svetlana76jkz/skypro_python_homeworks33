import pytest
from calculator import Calculator

def test_avg_empty_list(just_print_a_message, instence: Calculator):
    numbers = []
    assert instence.avg(numbers) == 0


def test_avg_positive_list(instence: Calculator, just_print_a_message):
    numbers = [1,2,3,4,5,6,7,8,9,5]
    assert instence.avg(numbers) == 5
