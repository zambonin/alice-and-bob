#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from random import getrandbits, randrange
from rsa import RSA


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


nbits = [2**i for i in range(6, 13)]
start = datetime.now()

for i in nbits:
    while True:
        p, q = getrandbits(i), getrandbits(i)
        if fermat(p, 100) and fermat(q, 100):
            end = datetime.now()
            print("Time: {}\tBits: {}\n{}\n".format(end - start, i, RSA(p, q)))
            break
