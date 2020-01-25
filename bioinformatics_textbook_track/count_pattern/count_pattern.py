def count_pattern(seq, p):
    return len([1 for i in range(0, len(seq) - len(p) + 1) if seq[i: i + len(p)] == p])


with open('dna.txt') as file:
    dna, patten = file.read().split()
    res = count_pattern(dna, patten)
    print(res)
