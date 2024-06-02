import pytest
from calculator import Calculator


def test_sum_positive_nums(just_print_a_message, instence: Calculator):
    assert instence.sum(4, 5) == 9


def test_sum_negative_nums(just_print_a_message, instence: Calculator):
    assert instence.sum(-6, -10) == -16


def test_sum_positive_and_negative_nums(just_print_a_message, instence: Calculator):
    assert instence.sum(-6, 6) == 0


def test_sum_float_nums(just_print_a_message, instence: Calculator):
    assert instence.sum(5.6, 4.3) == 9.899999999999999


def test_sum_zero_nums(just_print_a_message, instence: Calculator):
    assert instence.sum(6, 0) == 6


def test_div_pozitive_nums(just_print_a_message, instence: Calculator):
   assert instence.div(10, 2) == 5


def test_div_by_zero(just_print_a_message, instence: Calculator):
    with pytest.raises(ArithmeticError):
        instence.div(10, 0) == 10


def test_avg_empty_list(just_print_a_message, instence: Calculator):
    numbers = []
    assert instence.avg(numbers) == 0


def test_avg_positive_list(instence: Calculator, just_print_a_message):
    numbers = [1,2,3,4,5,6,7,8,9,5]
    assert instence.avg(numbers) == 5
