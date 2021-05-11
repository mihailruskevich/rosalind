from functools import reduce

NT_CODES = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}


def base4(n):
    while n > 0:
        yield n % 4
        n //= 4


def number_to_dna(n, length):
    dna = reduce(lambda s, c: s + NT_CODES[c], base4(n), '')
    return 'A' * (length - len(dna)) + dna[::-1]


with open('data.txt') as file:
    [i, k] = [int(v.strip()) for v in file]
    res = number_to_dna(i, k)
    print(res)
