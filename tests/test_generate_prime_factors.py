# pylint: disable=missing-docstring
"""
The test module for Prime Factors
"""
import pytest

from prime import generate_prime_factors


def test_string_values_are_rejected():
    with pytest.raises(ValueError):
        generate_prime_factors('banana')
