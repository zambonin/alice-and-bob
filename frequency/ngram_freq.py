#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import sys

from collections import Counter, OrderedDict

try:
    from matplotlib import pyplot as plt
except ImportError:
    pass


def ngram_frequency(n, text):
    digs = tuple(text[x:x + n] for x in range(len(text) - (n - 1)))

    return {k: v for k, v in Counter(digs).items() if ' ' not in k}


def show_output(freq, num, path):
    ord_dict = OrderedDict(sorted(freq.items(), key=lambda k: k[1],
                                  reverse=True)[:num])

    try:
        size = range(len(ord_dict))
        plt.hold(False)
        plt.bar(size, ord_dict.values(), align='center')
        plt.xticks(size, list(ord_dict.keys()))
        plt.autoscale()
        plt.savefig(path, bbox_inches='tight')
    except NameError:
        print("Common n-grams where n = {}:".format(
            len(list(ord_dict.keys())[0])))
        for i in ord_dict:
            step = max(ord_dict[i] for i in ord_dict) / len(ord_dict)
            bars = "▇" * int(ord_dict[i] / step)
            print("{}: {} ({})".format(i, bars, ord_dict[i]))

if __name__ == '__main__':
    arg = sys.argv[1]
    with open(arg) as raw:
        text = "".join(i.lower().replace('\n', ' ') for i in raw.readlines())
        pattern = re.compile('[^a-z ]+')
        simple = pattern.sub('', text)

        for n, m in zip([1, 2, 3], [26, 20, 15]):
            show_output(ngram_frequency(n, simple), m, 'n{}.png'.format(n))
