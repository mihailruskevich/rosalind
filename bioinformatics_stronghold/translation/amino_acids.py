from utils.constants import RNA_CODES

ACID_LEN = 3


def translate(rna):
    return [RNA_CODES[rna[i:i + ACID_LEN]] for i in range(0, len(rna) - ACID_LEN + 1, ACID_LEN)]


rna_seq = open('protein.txt').read()
protein = translate(rna_seq)
print(''.join(protein[:-1]))
