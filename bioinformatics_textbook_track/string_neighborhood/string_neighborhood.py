from itertools import product

from utils.common import hamming


def neighbors(s, d):
    return [''.join(mer) for mer in product('ACGT', repeat=len(s)) if hamming(mer, s) <= d]


with open('dna.txt') as file:
    dna, length = file.read().split()
    values = neighbors(dna, int(length))
    print(*values, sep='\n')
