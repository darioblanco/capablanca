# -*- coding: utf-8 -*-
# Copyright 2015, Dario Blanco

import pytest

from capablanca.cache import ThreatCache
from capablanca.piece import King


@pytest.fixture()
def threat_cache():
    return ThreatCache(3, 3)


def test_cache_hit(monkeypatch, threat_cache):
    """Should return threatened positions when there is a cache hit"""
    expected_threats = set([(0, 1), (1, 0), (1, 1)])

    def mocked_get_threats(self, current):
        assert False, "Cache miss when expecting a cache hit"

    threat_cache.cache = {'K:0,0': expected_threats}
    monkeypatch.setattr(King, 'get_threats', mocked_get_threats)

    assert threat_cache.get_threats('K', (0, 0)) == expected_threats


def test_cache_miss(monkeypatch, threat_cache):
    """Should return threatened positions when there is a cache miss"""
    expected_threats = set([(0, 1), (2, 0), (0, 0), (1, 1), (2, 1)])

    def mocked_get_threats(self, current):
        return expected_threats

    monkeypatch.setattr(King, 'get_threats', mocked_get_threats)

    assert threat_cache.get_threats('K', (1, 0)) == expected_threats
