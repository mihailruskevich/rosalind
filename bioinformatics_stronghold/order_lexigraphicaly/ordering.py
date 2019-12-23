from itertools import product


def order_map(a):
    return {c: i for i, c in enumerate(a)}


def ordered_combinations(a, n):
    order = order_map(a)
    strings = [''.join(p) for p in product(['', *a], repeat=n)]
    return sorted(set(strings), key=lambda v: [order[c] for c in v])


line1, line2 = open('alphabet.txt')
alphabet = line1.rstrip().split()
max_length = int(line2)

lines = ordered_combinations(alphabet, max_length)
print(*lines[1:], sep='\n')
