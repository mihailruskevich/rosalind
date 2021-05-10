def min_skew(dna):
    g, c, = 0, 0
    min_s, min_i = 0, []
    for i in range(0, len(dna)):
        c += 1 if dna[i] == 'C' else 0
        g += 1 if dna[i] == 'G' else 0
        s = g - c
        if s < min_s:
            min_s, min_i = s, [i + 1]
        elif s == min_s:
            min_i.append(i + 1)
    return min_i


with open('dna.txt') as [line]:
    res = min_skew(line)
    print(*res)
