from functools import reduce


def permutations(n, k):
    return reduce(lambda p, v: p * v, range(n, n - k, -1))


p = permutations(83, 8)
print(p)
print(p % 1000000)
