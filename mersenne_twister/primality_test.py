#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=C0103

"""primality_test.py

Simple implementations for the Fermat and Miller-Rabin primality tests.
"""

from __future__ import absolute_import
from random import randrange


def fermat(n, k):
    """
    The simplest probabilistic test to check whether a number is prime
    or not; it verifies the compositeness of the number through modular
    exponentiation.

    Args:
        n: number to test.
        k: number of times that `n` will be tested for primality.

    Returns:
        True means "probably prime", whereas False means "composite".
        Numbers known as Carmichael numbers are examples of false
        positives to this test.
    """
    if n <= 3:
        return True
    if n & 1 == 0:
        return False

    return all(pow(randrange(2, n - 1), n - 1, n) == 1 for _ in range(k))


def miller_rabin(n, k):
    """
    A primality test which is more complex than Fermat's. It is based
    on claims derived from Fermat's Little Theorem (a^(n-1) ≡ 1 (mod n)).

    Args:
        n: the number to be tested for primality.
        k: number of iterations (quantity of randomly chosen `a` integers).

    Returns:
        True means "probably prime", whereas False means "composite".
    """

    def composite(a, s, d, n):
        """
        Checks if a given number is composite through modular arithmetic.
        Consider that `n` is prime and `n > 2`. Hence, `n - 1` is even and
        `n - 1 = (2^s)d`.

        Args:
            a: a randomly chosen number; it is called a "witness" of `n` if
                a^d ≢ 1 (mod n) and
                a^((2^r)d) ≢ -1 (mod n) for all 0 <= r <= s - 1
                thereby classifying `n` as not prime.
            s, d: positive integers with `d` being odd, crucial to the
                  assertions above.
            n: the original number to be tested.

        Returns:
            True means "composite", whereas False means "probably prime".
        """
        x = pow(a, d, n)
        if x == 1:
            return True
        for _ in range(s):
            if x == n - 1:
                return True
            x = pow(x, 2, n)
        return x == n - 1

    if n <= 3:
        return True
    if n & 1 == 0:
        return False

    s, d = 0, n - 1
    while d & 1 == 0:
        s, d = s + 1, d >> 1

    return all(composite(randrange(2, n - 1), s, d, n) for _ in range(k))
