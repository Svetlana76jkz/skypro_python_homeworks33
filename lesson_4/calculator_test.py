import pytest
from calculator import Calculator

calculator = Calculator()

def test_sum_positive_nums(just_print_a_message):
    calculator = Calculator()
    res = calculator.sum(4, 5)
    assert res == 9

def test_sum_negative_nums(just_print_a_message):
    calculator = Calculator()
    res = calculator.sum(-6, -10)
    assert res == -16

def test_sum_positive_and_negative_nums(just_print_a_message):
    calculator = Calculator()
    res = calculator.sum(-6, 6)
    assert res == 0

def test_sum_float_nums(just_print_a_message):
    calculator = Calculator()
    res = calculator.sum(5.6, 4.3)
    res = round(res,1)
    assert res == 9.9

def test_sum_zero_nums(just_print_a_message):
    calculator = Calculator()
    res = calculator.sum(6, 0)
    assert res == 6

def test_div_pozitive_nums(just_print_a_message):
    calculator = Calculator()
    res = calculator.div(10, 2)
    assert res == 5

def test_div_by_zero(just_print_a_message):
    calculator = Calculator()
    with pytest.raises(ArithmeticError):
        calculator.div(10, 0)


def test_avg_empty_list(just_print_a_message):
    calculator = Calculator()
    numbers = []
    res = calculator.avg(numbers)
    assert res == 0

def test_avg_positive_list(just_print_a_message):
    calculator = Calculator()
    numbers = [1,2,3,4,5,6,7,8,9,5]
    res = calculator.avg(numbers)
    assert res == 5
