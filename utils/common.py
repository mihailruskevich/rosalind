def reverse_complement(dna: str) -> str:
    return dna[::-1] \
        .replace('A', 't') \
        .replace('C', 'g') \
        .replace('G', 'C') \
        .replace('T', 'A') \
        .upper()


def reverse_complement_2(dna: str) -> str:
    return dna[::-1].translate(str.maketrans('ACGT', 'TGCA'))


def gc_content(dna: str) -> float:
    gc_seq = [nt for nt in dna if nt in 'GC']
    return float(len(gc_seq)) / len(dna)


def int_list(str_value, sep=' ') -> list[int]:
    return list(map(int, str_value.split(sep)))


def float_list(str_value, sep=' ') -> list[float]:
    return list(map(float, str_value.split(sep)))


def hamming(p: str, q: str) -> int:
    return sum(1 for x, y in zip(p, q) if x != y)
