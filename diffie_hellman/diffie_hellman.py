#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""diffie_hellman.py

Simple class implementation for the Diffie-Hellman key exchange.
"""


class DiffieHellman:
    """
    Diffie–Hellman key exchange is a method of securely exchanging
    cryptographic keys over a public channel; it should provide enough
    security that there would be no way of recovering the plain text
    from traffic encoded by the shared encryption key between two parties.

    Detailed information about DH can be found on the original paper:
    https://www-ee.stanford.edu/~hellman/publications/24.pdf

    A simple explanation for DH: http://security.stackexchange.com/a/45971
    """

    def __init__(self, private, p, g):
        """
        Initializes the DiffieHellman object with the following attributes:

            private: the user's private key; generally, this should be
                     generated through cryptographically secure means,
                     perhaps by the program itself.
            p: a prime number, called the modulus.
            g: a primitive root modulo p, called the base.
        """
        self.private = private
        self._p = p
        self._g = g

    def __str__(self):
        """Pretty-prints the attributes from the Diffie-Hellman object."""
        return (
            "Private key:    {}\n"
            "Prime number:   {}\n"
            "Primitive root: {}\n"
            "Public key:     {}".format(
                self._p, self._g, self.private, self.gen_public_key()
            )
        )

    def gen_public_key(self):
        """
        Generates a number that can be freely distributed, for it is too
        difficult to derive the secret part from it (the exponent, which is
        the private key); solving this equation would imply solving the
        discrete logarithm problem efficiently.

        Returns:
            g**a mod p -- the public key for this party.
        """
        return pow(self._g, self.private, self._p)

    def gen_shared_secret(self, key):
        """
        A shared secret is a value derived from the public key freely
        distributed; it can be used to ascertain the validity of messages
        shared by the two parties.

        Args:
            key: public key from the second party.

        Returns:
            (g**a mod p)**b mod p = g**ab mod p = g**ba mod p -- which
            shows that the shared secret is indeed the same.
        """
        return pow(key, self.private, self._p)
