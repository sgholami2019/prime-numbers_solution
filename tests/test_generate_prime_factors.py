# pylint: disable=missing-docstring
"""
The test module for Prime Factors
"""
import pytest

from prime import generate_prime_factors


def test_string_values_are_rejected():
    with pytest.raises(ValueError):
        generate_prime_factors('banana')


def test_called_with_one():
    assert generate_prime_factors(1) == []


def test_called_with_two():
    assert generate_prime_factors(2) == [2]


def test_called_with_three():
    assert generate_prime_factors(3) == [3]


def test_called_with_four():
    assert generate_prime_factors(4) == [2, 2]
