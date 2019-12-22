from functools import reduce


def pairs(n, k):
    return reduce(lambda p, _: (p[1], p[1] + k * p[0]), range(n - 1), (1, 1))[0]


months = 29
produces = 3
pair_count = pairs(months, produces)
print(pair_count)
