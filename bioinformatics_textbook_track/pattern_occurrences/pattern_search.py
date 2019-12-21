
def find(seq, p):
    indices = []
    i = seq.find(p)
    while i != -1:
        indices.append(i)
        i = seq.find(p, i + 1)
    return indices


pattern, dna = open('dna.txt')
pattern = pattern.rstrip()
res = find(dna, pattern)
print(*res)
