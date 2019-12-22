from functools import reduce
from math import log10

from utils.common import float_list


def nt_prob_map(gc_value):
    return {
        'A': (1 - gc_value) / 2,
        'C': gc_value / 2,
        'G': gc_value / 2,
        'T': (1 - gc_value) / 2
    }


def seq_prob(s, gc):
    pr_map = nt_prob_map(gc)
    return reduce(lambda p, v: p * pr_map[v], s, 1)


def seq_prob_list(s, gc_list):
    return [log10(seq_prob(s, gc)) for gc in gc_list]


line1, line2 = open('data.txt')
seq = line1.rstrip()
gc_values = float_list(line2)

prob_list = seq_prob_list(seq, gc_values)
print(' '.join(map(str, prob_list)))
