from functools import reduce


def probability(seq, x, n):
    a_t = (1 - x) / 2
    g_c = x / 2
    p_map = {'A': a_t, 'C': g_c, 'G': g_c, 'T': a_t}
    r = reduce(lambda p, nt: p * p_map[nt], seq, 1)
    return 1 - (1 - r) ** n


line1, dna = open('data.txt')
am, gc = line1.rstrip().split(' ')
amount, gc_content = int(am), float(gc)

res = probability(dna, gc_content, amount)
print(res)
