from itertools import product


def increment(x, l):
    i = len(x) - 1
    while i >= 0 and (x[i] + 1) // l != 0:
        x[i] = 0
        i = i - 1
    x[i] += 1


def permutations(a, n):
    res = []
    indices = [0] * n
    for _ in range(len(a) ** n):
        res.append(''.join(map(a.__getitem__, indices)))
        increment(indices, len(a))
    return res


def permutations_2(a, n):
    return map(''.join, product(*[a] * n))


file = open('alphabet.txt')
alphabet = next(file).rstrip().split(' ')
size = int(next(file))

# result = permutations(alphabet, size)
result = permutations_2(alphabet, size)
for s in result:
    print(s)
