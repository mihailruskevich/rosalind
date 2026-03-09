import numpy as np


def probability_of_one_or_two_allele(p_aa):
    p_a = p_aa ** 0.5
    return p_aa + 2 * p_a * (1 - p_a)


with open('data.txt') as [line]:
    p_aa_list = np.fromstring(line, dtype=float, sep=' ')
    p_array = probability_of_one_or_two_allele(p_aa_list)
    np.savetxt('res.txt', p_array, fmt='%.3f', newline=' ')
