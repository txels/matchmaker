from hamcrest import *
from matchmaker.decorators import match_maker

not_ = is_not


@match_maker
def is_four(item):
    """Is four"""
    return item == 4


@match_maker
def is_five(item):
    return item == 5


@match_maker
def is_even(item):
    """Is even"""
    return item % 2 == 0


def test_is_four():
    assert_that(4, is_four())


def test_is_not_four():
    assert_that(5, not_(is_four()))


def test_is_five():
    assert_that(5, is_five())


def test_is_five_or_four():
    assert_that(4, any_of(is_four(), is_five()))


def _is_five_or_even(item):
    assert_that(item, any_of(is_five(), is_even()))


def test_is_five_or_even():
    for value in [0, 2, 4, 5, 6, 8]:
        yield _is_five_or_even, value
