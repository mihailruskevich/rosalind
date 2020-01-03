from functools import reduce
import numpy as np


def probability_map(x):
    a_t, g_c = (1 - x) / 2, x / 2
    return {'A': a_t, 'C': g_c, 'G': g_c, 'T': a_t}


def expected_matches(seq, n, gc):
    p_map = probability_map(gc)
    r = reduce(lambda p, nt: p * p_map[nt], seq, 1)
    return r * (n - len(seq) + 1)


with open('data.txt') as (length, dna, arr):
    dna = dna.rstrip()
    gc_values = np.fromstring(arr, sep=' ')
    expected_matches_list = expected_matches(dna, int(length), gc_values)
    expected_matches_list.tofile('res.txt', sep=' ')
