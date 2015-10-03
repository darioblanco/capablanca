# -*- coding: utf-8 -*-
# Copyright 2015, Dario Blanco

import pytest

from click.testing import CliRunner


@pytest.fixture()
def runner():
    """Creates a CliRunner instance for any test that needs it"""
    return CliRunner()
