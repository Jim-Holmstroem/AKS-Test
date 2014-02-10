from __future__ import print_function, division

from sympy import Symbol, ZZ


def is_prime(p):
    """Check if p is prime.

    Parameters
    ----------
    p : int
        The integer to check if prime.

    Returns
    -------
    is_prime : bool
        p is prime.
    """
    assert(p > 0)
    if p == 1: return False

    x = Symbol('x')
    poly = ((x - 1) ** p - (x ** p - 1))
    is_prime = (poly / p).as_poly().domain == ZZ

    return is_prime
