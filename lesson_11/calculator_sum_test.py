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
