#!/usr/bin/env python
# -*- coding: utf-8 -*-


class MT19937(object):
    """
    The Mersenne Twister is the most widely used pseudorandom number generator
    (PRNG). The common version is based on the Mersenne prime 2^19937 - 1,
    (which is also the period of MT) and uses a 32 bit word length.

    Detailed information about MT can be found on the original paper:
    http://www.math.sci.hiroshima-u.ac.jp/~m-mat/MT/ARTICLES/mt.pdf

    And the reference C code:
    http://www.math.sci.hiroshima-u.ac.jp/~m-mat/MT/MT2002/CODES/mt19937ar.c
    """
    def __init__(self, seed, w, n, m, r, a, u, d, s, b, t, c, l, f):
        """
        Initializes the MT19937 object with the following attributes:

            seed: the initial seed for the algorithm.
            w: number of bits of each word in the state sequence.
            n: number of elements in the state sequence. It determines the
               degree of recurrence in the generated series.
            m: on each twist, the elements are transformed using other values
               in the sequence that are `m` elements away. It should be less
               than or equal to `n`.
            r: the number of bits that mark the separation point of words on
               each twist. It should be lower than or equal to `w`.
            a: the XOR mask to be applied as the linear function on each twist.
               It should be lower than `1u << w`.
            s, t, u, l: tempering shift values for the scrambling operation
                        used by the generation algorithm. They should be lower
                        than `1u << w`.
            b, c, d: tempering bit mask values for the scrambling operation
                     used by the generation algorithm. They should be lower
                     than `1u << w`.
            f: initialization multiplier used to seed the state sequence when a
               single value is used as seed.
        """
        self.mt = [None] * n
        self.index = n + 1
        self.lower_mask = (1 << r) - 1
        self.upper_mask = self.lowest_n_bits(~(self.lower_mask), w)
        self.w = w
        self.n = n
        self.m = m
        self.r = r
        self.a = a
        self.u = u
        self.d = d
        self.s = s
        self.b = b
        self.t = t
        self.c = c
        self.l = l
        self.f = f
        self.seed_init(seed)

    def lowest_n_bits(self, num, n_bits):
        """
        Utility function that creates a 0x111... mask and applies it to the
        desired number.

        Args:
            num: the number to be analyzed.
            n_bits: number of bits to be retrieved.

        Returns:
            The lowest n bits of `num`.
        """
        return num & (2**n_bits - 1)

    def seed_init(self, seed):
        """
        Creates a vector of `n` integers to be used as the state sequence from
        which future iterations are produced.

        Args:
            seed: the initial seed for the algorithm. Note that this algorithm
                  could be adapted to accept a list of integer seeds that could
                  be filled with other elements until its length reaches `n`.
        """
        self.index = self.n
        self.mt[0] = seed
        for i in range(1, self.n):
            prev = self.mt[i - 1]
            self.mt[i] = self.lowest_n_bits(
                self.f * (prev ^ (prev >> (self.w - 2)) + i), self.w)

    def generate(self):
        """
        Performs tempering with bit over the bits received from the `twist`
        procedure with bit mask values and shifts.

        Returns:
            a pseudorandom integer `y` inside the interval [0, 2^`w` - 1).
        """
        if self.index >= self.n:
            self.twist()

        y = self.mt[self.index]
        y ^= ((y >> self.u) & self.d)
        y ^= ((y << self.s) & self.b)
        y ^= ((y << self.t) & self.c)
        y ^= (y >> self.l)

        self.index += 1

        return self.lowest_n_bits(y, self.w)

    def twist(self):
        """
        Generates the next `n` values from the `x` series based on a
        recurrence relation.
        """
        for i in range(self.n):
            x = ((self.mt[i] & self.upper_mask) +
                 (self.mt[(i + 1) % self.n] & self.lower_mask))
            xA = x >> 1

            if (x % 2) == 0:
                xA ^= self.a

            self.mt[i] = self.mt[(i + self.m) % self.n] ^ xA

        self.index = 0
