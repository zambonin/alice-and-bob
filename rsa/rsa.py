#!/usr/bin/env python
# -*- coding: utf-8 -*-


class RSA(object):
    """
    RSA is one of the first practical public-key cryptosystems. The encryption
    key is public and the decryption key is secret. This asymmetry is based on
    the practical difficulty of factoring the product of two large prime
    numbers, used to create such keys.

    Detailed information about RSA can be found on the original paper:
    http://people.csail.mit.edu/rivest/Rsapaper.pdf

    A simple explanation for RSA: http://math.stackexchange.com/a/20193
    """
    def __init__(self, p, q):
        """
        Initializes the RSA object with the following attributes:

            p, q:  two randomly generated primes with roughly the same size.
                   Should be kept private.

        The other attributes are explained below:

            n:     the product of the input primes and the common modulo
                   operator for encryption and decryption.
            phi_n: result of Euler's totient function applied to `n`. Crucial
                   for the generation of the encryption/decryption exponents,
                   should be kept private.
            e:     the encryption exponent, generally shared with the public
                   along with `n`. RFC4871 determines this number to be 65537,
                   however it can be any reasonably large coprime to `n`.
            d:     the decryption exponent. It is the modular multiplicative
                   inverse of `e` modulo `phi_n`, Should be kept private.
        """
        self.p = p
        self.q = q
        self.n = self.p * self.q
        self.phi_n = (self.p - 1) * (self.q - 1)
        self.e = 65537
        self.d = self.inv_mod(self.e, self.phi_n)

    def __str__(self):
        """Pretty-prints the attributes from the RSA object."""
        return "Your public key is {}.\nYour private key is {}.".format(
            (self.e, self.n), (self.d, self.n))

    def extended_gcd(self, a, b):
        """
        The extended Euclidean algorithm computes `gcd(a, b)` and the integers
        `x` and `y` on the Bézout's identity (ax + by = gcd(a, b)).

        Args:
            a, b: two integers.

        Returns:
            `gcd(a, b)`, `x` and `y` such that the above identity is true.
        """
        gcd, remainder = abs(a), abs(b)
        x, y, old_x, old_y = 1, 1, 0, 0

        while remainder:
            gcd, (quotient, remainder) = remainder, divmod(gcd, remainder)
            old_x, x = x - quotient*old_x, old_x
            old_y, y = y - quotient*old_y, old_y

        return gcd, x, y

    def inv_mod(self, a, m):
        """
        The modular multiplicative inverse of an integer `a` modulo `m` is an
        integer `x` such that a*x ≡ 1 (mod m). It the multiplicative inverse in
        the ring of integers modulo `m`.

        Args:
            a: the number to be inverted.
            m: the integer for the modulo operator.

        Returns:
            a^(-1) (mod m).
        """
        g, x, y = self.extended_gcd(a, m)
        return int(x % m)

    def encrypt(self, message):
        """
        Encrypt a message with RSA.

        Args:
            message: a string, that will be decoded to a list of ASCII ordinals
                     and those will be individually encoded; or an integer
                     smaller than `n'.

        Returns:
            m^e (mod n), where `m` is the message encoded to an integer.
        """
        if isinstance(message, str):
            return [pow(ord(i), self.e, self.n) for i in message]
        elif isinstance(message, int):
            assert message < self.n, "Integer has to be smaller than `n`."
            return pow(message, self.e, self.n)

    def decrypt(self, message):
        """
        Decrypt a message encoded with RSA.

        Args:
            message: a list of ASCII ordinals or an integer.

        Returns:
            c^d (mod n), where `c` is the cipher text.
        """
        if isinstance(message, list):
            return "".join(chr(pow(i, self.d, self.n)) for i in message)
        elif isinstance(message, int):
            return pow(message, self.d, self.n)
