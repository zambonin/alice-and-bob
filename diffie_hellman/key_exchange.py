#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=C0330

"""key_exchange.py

Test script for Diffie-Hellman implemented within this folder.
"""

from __future__ import absolute_import
from random import getrandbits
from diffie_hellman import DiffieHellman

XA, XB = getrandbits(512), getrandbits(512)

for i in [
    (589_559_306_225_789_680_238_449, 99_848_060_646_461_381_236_408),
    (1_076_504_068_900_685_093_590_721, 594_761_277_746_183_138_644_459),
]:

    alice = DiffieHellman(XA, *i)
    bob = DiffieHellman(XB, *i)

    A = alice.gen_shared_secret(bob.gen_public_key())
    B = bob.gen_shared_secret(alice.gen_public_key())

    assert A == B
