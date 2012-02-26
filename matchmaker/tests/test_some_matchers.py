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


@match_maker
def ends_like(item, arg1):
    """String that ends like '{0}'"""
    return item.endswith(arg1[-3:])


def test_ends_like():
    assert_that('hello', ends_like('trello'))


def test_not_ends_like():
    assert_that('hellou', not_(ends_like('trello')))


def test_ends_like_composite():
    assert_that('hello', any_of(ends_like('bella'), ends_like('chello')))
