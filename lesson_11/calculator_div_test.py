import pytest
from calculator import Calculator


def test_div_pozitive_nums(just_print_a_message, instence: Calculator):
   assert instence.div(10, 2) == 5


def test_div_by_zero(just_print_a_message, instence: Calculator):
    with pytest.raises(ArithmeticError):
        instence.div(10, 0) == 10
