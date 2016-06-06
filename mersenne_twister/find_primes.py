#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mt19937 import MT19937
from primality_test import miller_rabin
from datetime import datetime

mt19937_32 = (624, 397, 31, 0x9908b0df, 11, 0xffffffff, 7, 0x9d2c5680,
              15, 0xefc60000, 18, 1812433253)
start = datetime.now()

for i in [i*100 for i in range(1, 40)]:
    for j in range(10000):
        n = MT19937(datetime.now().microsecond, i, *mt19937_32).generate()
        if miller_rabin(n, 10):
            end = datetime.now()
            print("Time: {}\tBits: {}\nNumber: {}".format(end - start, i, n))
            break
