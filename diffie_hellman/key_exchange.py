#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""key_exchange.py

Test script for Diffie-Hellman implemented within this folder.
"""

from __future__ import absolute_import
from random import getrandbits
from diffie_hellman import DiffieHellman

XA, XB = getrandbits(512), getrandbits(512)

for i in [
    (589559306225789680238449, 99848060646461381236408),
    (1076504068900685093590721, 594761277746183138644459),
]:

    alice = DiffieHellman(XA, *i)
    bob = DiffieHellman(XB, *i)

    A = alice.gen_shared_secret(bob.gen_public_key())
    B = bob.gen_shared_secret(alice.gen_public_key())

    assert A == B
