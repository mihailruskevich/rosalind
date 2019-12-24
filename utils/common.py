
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


def int_list(str_value):
    return list(map(int, str_value.split(' ')))


def float_list(str_value):
    return list(map(float, str_value.split(' ')))


def hamming(p, q):
    return sum(1 for x, y in zip(p, q) if x != y)