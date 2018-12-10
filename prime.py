"""
prime.py -- Write the application code here
"""
def generate_prime_factors(value):
    """Returns a list of primes."""
    if not isinstance(value, int):
        raise ValueError()

    primes = []
    if value % 2 == 0:
        primes.append(2)
        value /= 2
    if value > 1:
        primes.append(value)

    return primes
