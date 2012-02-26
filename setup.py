#!/usr/bin/env python
# # coding: utf-8

from setuptools import setup
from matchmaker import __version__

LONG_DESC = """
Decorators that simplify the creation of Hamcrest matchers.

From a function (with an optional appropriate docstring), create
hamcrest matchers with minimum extra coding. 

Examples::
    
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
"""

setup(
    name='matchmaker',
    description='Easy creation of hamcrest matchers',
    long_description=LONG_DESC,
    version=__version__,
    author='Carles Barrobés',
    author_email='carles@barrobes.com',
    url='https://github.com/txels/matchmaker',
    packages=['matchmaker'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Testing',
    ],
)
