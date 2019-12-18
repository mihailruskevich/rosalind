from itertools import product

from utils.fasta import fasta_sequences


def k_mer_list(a):
    return [''.join(mer) for mer in product(*[a] * 4)]


def count_k_mer(seq, k_mer):
    k_len = len(k_mer)
    occurrences = 0
    for i in range(0, len(seq) - k_len + 1):
        if seq[i: i + k_len] == k_mer:
            occurrences += 1
    return occurrences


def k_mer_composition(seq, a):
    count_k_mer(seq, 'ACGT')
    return [count_k_mer(seq, k_mer) for k_mer in k_mer_list(a)]


file = open('dna.fas')
_, dna = next(fasta_sequences(file))

composition_string = k_mer_composition(dna, 'ACGT')
res = ' '.join(map(str, composition_string))
open('res.txt', 'w').write(res)
