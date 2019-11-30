
def reverse_complement(dna):
    return dna[::-1] \
        .replace('A', 't') \
        .replace('C', 'g') \
        .replace('G', 'C') \
        .replace('T', 'A') \
        .upper()


def reverse_complement_2(dna):
    return dna[::-1].translate(str.maketrans('ACGT', 'TGCA'))


def gc_content(dna):
    gc_seq = [nt for nt in dna if nt in 'GC']
    return float(len(gc_seq)) / len(dna)
