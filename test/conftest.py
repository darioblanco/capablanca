# -*- coding: utf-8 -*-
# Copyright 2015, Dario Blanco

import pytest

from click.testing import CliRunner


@pytest.fixture()
def runner():
    """Creates a CliRunner instance for any test that needs it"""
    return CliRunner()


def pytest_addoption(parser):
    """Accepts a new pytest console parameter"""
    parser.addoption("--test-type", action="store", default="unit",
                     choices=["unit", "integration"],
                     help="only run tests matching the TYPE name.")


def pytest_configure(config):
    """Registers an additional pytest marker"""
    config.addinivalue_line(
        "markers", "testtype(type): mark test as unit or integration")


def pytest_runtest_setup(item):
    """Executes pytest run with the custom marker"""
    type_marker = item.get_marker("testtype")
    if type_marker is not None:
        envname = type_marker.args[0]
    else:
        envname = "unit"

    if envname != item.config.getoption("--test-type"):
        pytest.skip(
            "Test skipped, requires --test-type {}".format(envname))
