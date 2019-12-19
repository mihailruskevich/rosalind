from functools import reduce

T = {
    ('A', 'A'): 0.393,
    ('A', 'B'): 0.607,
    ('B', 'A'): 0.511,
    ('B', 'B'): 0.489
}


def probability(s):
    return reduce(lambda p, v: p * T[v], zip(s, s[1:]), 0.5)


path = open('path.txt').readline()
result = probability(path)
print(result)
