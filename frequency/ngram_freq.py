#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""ngram_freq.py

Frequency analysis for 1-, 2- and 3-word groupings.
"""

from __future__ import absolute_import, division
from re import compile as _compile
from collections import Counter, OrderedDict
from sys import argv

try:
    from matplotlib import pyplot as plt
except ImportError:
    pass


def ngram_frequency(_n, text):
    """Count digraphs from a string and organize this into a dictionary."""
    digs = tuple(text[x : x + _n] for x in range(len(text) - (_n - 1)))
    return {k: v for k, v in Counter(digs).items() if " " not in k}


def show_output(freq, num, path):
    """Create graphs for n-gram groupings."""
    ord_dict = OrderedDict(sorted(freq.items(), key=lambda k: k[1], reverse=True)[:num])

    try:
        size = list(range(len(ord_dict)))
        plt.clf()
        plt.bar(size, list(ord_dict.values()), align="center")
        plt.xticks(size, list(ord_dict.keys()))
        plt.autoscale()
        plt.savefig(path, bbox_inches="tight")
    except NameError:
        print("Common n-grams where n = {}:".format(len(list(ord_dict.keys())[0])))
        for i in ord_dict:
            step = max(ord_dict[i] for i in ord_dict) / len(ord_dict)
            bars = "▇" * int(ord_dict[i] / step)
            print("{}: {} ({})".format(i, bars, ord_dict[i]))


if __name__ == "__main__":
    if len(argv) != 2:
        raise SystemExit("Invalid number of parameters!")
    with open(argv[1]) as raw:
        TEXT = "".join(i.lower().replace("\n", " ") for i in raw.readlines())
        SIMPLE = _compile("[^a-z ]+").sub("", TEXT)

        for n, m in zip([1, 2, 3], [26, 20, 15]):
            show_output(ngram_frequency(n, SIMPLE), m, "n{}.png".format(n))
