from utils.fasta import fasta_sequences
from math import perm as p


def max_matching_count(seq):
    a, c, g, u = seq.count('A'), \
                 seq.count('C'), \
                 seq.count('G'), \
                 seq.count('U')
    return (p(a, u) if a > u else p(u, a)) * (p(c, g) if c > g else p(g, c))


with open('rna.fas') as file:
    [(_, rna)] = fasta_sequences(file)
    count = max_matching_count(rna)
    print(count)
