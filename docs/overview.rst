Getting Started
===============

The only thing you will need is a function that takes a minimum of one
parameter and returns a boolean. The first parameter will be used for
the value to be matched, i.e. the first parameter to ``assert_that``.
The rest of parameters are arbitrary depending on your matcher.

.. code-block:: python

    @matcher
    def my_function(item, arg1):
        # Perform some check that item matches arg1
        etc...


It is recommended that you create a docstring for your function. If one
exists, it is used as a descriptive string for the case where matching fails.
If the string contains string formatting placeholders, they will be used
to fill in the matcher functions arguments 1 to *n*.

In the absence of a docstring, ``matchmaker`` will adapt the function name
by replacing underscores with spaces and capitalising the first word.

Usage Examples
--------------

A few matchers::
    
    from matchmaker import matcher

    @matcher
    def is_even(item):
        return item % 2 == 0

    @matcher
    def ends_like(item, data, length=3):
        "String whose last {1} chars match those for '{0}'"
        return item.endswith(data[-length:])

You can then use these in your tests as::

    assert_that(number, is_even())
    assert_that(word, ends_like(other_word, 4))

Errors will display as::

    AssertionError:
    Expected: Is even
         but: was <3>

     AssertionError:
     Expected: String whose last 4 chars match those for 'cello'
          but: was 'hullo'
