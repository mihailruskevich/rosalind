from utils.fasta import fasta_sequences
from math import factorial as f


def perfect_matching_count(seq):
    return f(seq.count('A')) * f(seq.count('C'))


with open('rna.fas') as file:
    [(_, rna)] = fasta_sequences(file)
    count = perfect_matching_count(rna)
    print(count)
