from __future__ import print_function, division

import string

from operator import ge
from itertools import chain, imap, takewhile
from functools import partial

from nose.tools import assert_true, assert_false

from ..akstest import is_prime


test_cutoff = 150


parse_file = lambda open_file:\
    takewhile(
        partial(ge, test_cutoff),
        imap(
            int,
            chain.from_iterable(
                imap(
                    string.split,
                    open_file
                )
            )
        )
    )


def test_is_prime():
    def assert_is_prime(p):
        assert_true(is_prime(p))

    with open('primes.dat') as prime_file:
        for prime in parse_file(prime_file):
            yield assert_is_prime, prime


def test_is_not_prime():
    def assert_is_not_prime(p):
        assert_false(is_prime(p))

    with open('non_primes.dat') as non_prime_file:
        for non_prime in parse_file(non_prime_file):
            yield assert_is_not_prime, non_prime
