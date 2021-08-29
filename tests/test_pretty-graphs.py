# Copyright (C) 2021 ''

import pkg_resources

import pytest

try:
    from pretty-graphs import pretty-graphs
except pkg_resources.DistributionNotFound:
    raise ImportError("did you run 'pip install -e .' for your project")


def test_import():
    pretty-graphs.say_hello()


"""
you are looking for setup / teardown methods? py.test has fixtures:
    http://doc.pytest.org/en/latest/fixture.html
you find examples below
"""


@pytest.yield_fixture
def one():
    print("setup")
    yield 1
    print("teardown")


def test_something(one):
    assert one == 1
