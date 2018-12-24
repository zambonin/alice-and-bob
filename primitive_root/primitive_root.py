#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=C0103

"""primitive_root.py

Helper functions used to find primitive roots modulo n, also known as
generators of the multiplicative group of integers modulo n.
"""

from __future__ import absolute_import
from random import randrange


def gcd(a, b):
    """
    Recursive Euclidean algorithm; an efficient method of computing the
    greatest common divisor (GCD) between two numbers. More information
    about the mathematical procedures can be found on the literature.

    Args:
        a, b: integers to be divided repeatedly.

    Returns:
        A recursive call that calculates the GCD repeatedly, with each
        number getting smaller until the remainder is zero.
    """
    return gcd(b, a % b) if b else a


def euler_phi(n):
    """
    Euler's totient function (φ(n)); the number of integers in [1, n]
    such that GCD(n, k) = 1, or the number of coprimes of `n`.

    Args:
        n: integer that limits the range of coprime counting.

    Returns:
        The number of coprimes of `n`.
    """
    return sum(gcd(i, n) == 1 for i in range(n))


def prime_factors(n):
    """
    Calculates all the prime factors of `n` until its square root is reached.

    Args:
        n: the number to be factorized.

    Returns:
        The sorted list of unique prime factors of `n`.
    """
    factors = set()
    i = 2

    while i ** 2 <= n:
        if n % i == 0:
            n = n // i
            factors.add(i)
        else:
            i += 1
    factors.add(n)

    return sorted(factors)


def prim_roots(n, singular=True):
    """
    Finds one or all primitive roots of an integer `n`.

    Args:
        n: prime integer to be operated.
        singular: a boolean value that nullifies the while and outputs
                  only the first primitive root found.

    Returns:
        One or all of the primitive roots of a number.
    """
    p = euler_phi(n)
    factors = prime_factors(p)
    limit, p_roots = 1 if singular else euler_phi(p), set()

    while len(p_roots) != limit:
        a = randrange(1, n)
        if all(pow(a, p // f, n) != 1 for f in factors):
            p_roots.add(a)

    return sorted(p_roots)
