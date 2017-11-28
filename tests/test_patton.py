# -*- coding: utf-8 -*-
"""
test_patton
----------------------------------
Tests for `patton` module.
"""


import pytest

from patton.dal.database import engine


@pytest.fixture
def response():
    """
    Sample pytest fixture.
    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    return 'response'


def test_content(response):
    """
    Sample pytest test function with the pytest fixture as an argument.
    """
    assert engine is not None
