"""
prime.py -- Write the application code here
"""
def generate_prime_factors(value):
    """Returns a list of primes."""
    if not isinstance(value, int):
        raise ValueError()

    primes = []
    factor = 2
    while factor <= value:
        while value % factor == 0:
            primes.append(factor)
            value /= factor

        factor += 1

    return primes
