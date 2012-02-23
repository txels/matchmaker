from hamcrest import *
from .decorators import match_maker

items = [1, 2, 3, 4]
not_ = is_not


def test_in():
    assert_that(4, is_in(items))

def test_out():
    assert_that(5, not_(is_in(items)))

@match_maker
def is_four(item):
    """Is four"""
    return item == 4

@match_maker
def is_five(item):
    return item == 5

def test_is_four():
    assert_that(4, is_four())

def test_is_five():
    assert_that(5, is_five())
