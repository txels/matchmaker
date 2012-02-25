``matchmaker`` makes it easier to write hamcrest matchers with minimum fuss.

Example usage:

```python

    from hamcrest import *
    from matchmaker.decorators import match_maker

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

    @match_maker
    def is_odd(item):
        """Is odd"""
        return item % 2 == 1

    def test_is_four():
        assert_that(4, is_four())

    def test_is_five():
        assert_that(5, is_five())

    def test_is_five_or_four():
        assert_that(4, any_of(is_four(), is_five()))

    def _is_odd_or_even(item):
        assert_that(item, any_of(is_odd(), is_even()))

    def test_is_odd_or_even():
        for value in range(10):
            yield _is_odd_or_even, value
```
