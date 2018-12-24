#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=C0103

"""find_primes.py

Naïve script to generate pseudorandom numbers and test their primality.
"""

from __future__ import absolute_import
from datetime import datetime
from mt19937 import MT19937
from primality_test import miller_rabin

mt19937_32 = (
    624,
    397,
    31,
    0x9908B0DF,
    11,
    0xFFFFFFFF,
    7,
    0x9D2C5680,
    15,
    0xEFC60000,
    18,
    1812433253,
)
start = datetime.now()

for i in range(100, 4000, 100):
    for j in range(10000):
        n = MT19937(datetime.now().microsecond, i, *mt19937_32).generate()
        if miller_rabin(n, 10):
            end = datetime.now()
            print("Time: {}\tBits: {}\nNumber: {}".format(end - start, i, n))
            break
