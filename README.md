``matchmaker`` makes it easier to write hamcrest matchers with minimum fuss.

It includes decorators that turn simple functions that return booleans
into hamcrest matchers. The docstring, or in its absence, the function
name, is used as descriptive string for the case where matching fails.

This is a silly example of usage, just to see how it looks:

```python
from hamcrest import *
from matchmaker import matcher

@matcher
def is_four(item):
    """Is four"""
    return item == 4

@matcher
def is_even(item):
    """Is even"""
    return item % 2 == 0

def test_is_four():
    assert_that(4, is_four())

def test_is_four_or_even():
    assert_that(8, any_of(is_four(), is_even()))
```
