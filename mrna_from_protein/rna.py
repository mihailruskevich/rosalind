from functools import reduce

from utils.constants import RNA_CODES

duplicates = list(RNA_CODES.values())
acids = set(RNA_CODES.values())
ACID_AMOUNTS = {acid: duplicates.count(acid) for acid in acids}


def rna_variants(seq):
    return reduce(lambda res, v: res * ACID_AMOUNTS[v], seq, 1)


protein_seq = open('protein.txt').read()
amount = rna_variants(protein_seq) * 3
print(amount % 1000000)
