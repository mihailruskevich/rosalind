NT_CODES = {'A': 0, 'C': 1, 'G': 2, 'T': 3}


def dna_to_number(dna):
    k = len(dna)
    return sum([NT_CODES[nt] * 4 ** (k - i - 1) for i, nt in enumerate(dna)])


with open('dna.txt') as [line]:
    number = dna_to_number(line)
    print(number)
