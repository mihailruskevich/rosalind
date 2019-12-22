from itertools import chain

from Bio.Seq import translate

# Different codon tables
# 1-6, 9-16, and 21-23
TABLE_IDS = chain(
    range(1, 7),
    range(9, 17),
    range(21, 24)
)


def genetic_table_index(seq, p):
    return next(filter(lambda i: translate(seq, table=i, to_stop=True) == p, TABLE_IDS), None)


dna, prot = open('dna.txt')
dna = dna.rstrip()
table_index = genetic_table_index(dna, prot)
print(table_index)
