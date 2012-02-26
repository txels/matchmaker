#!/usr/bin/env python
# # coding: utf-8

from setuptools import setup
from matchmaker import __version__

LONG_DESC = """
Decorators that simplify the creation of Hamcrest matchers.

From a function (with an optional appropriate docstring), create
hamcrest matchers with minimum extra coding. 

Examples::
    
    from matchmaker.decorators import match_maker

    @match_maker
    def is_even(item):
        return item % 2 == 0

    @match_maker
        def ends_like(item, data, length=3):
        "String whose last {1} chars match those for '{0}'"
        return item.endswith(data[-length:])
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
