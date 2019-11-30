from functools import reduce

INITIAL_MAP = {'A': 0, 'C': 0, 'G': 0, 'T': 0}


def count_nt(dna):
    return reduce(lambda nt_map, nt: {**nt_map, nt: nt_map[nt] + 1}, dna, INITIAL_MAP)


def prepare_result(nt_map):
    return ' '.join(map(str, nt_map.values()))


loaded_dna = open('rosalind_dna.txt').read()
nt_count = prepare_result(count_nt(loaded_dna))
open('rosalind_result.txt', 'w').write(nt_count)
