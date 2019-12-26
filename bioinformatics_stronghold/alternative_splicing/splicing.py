from math import factorial as f


def c(n, k):
    return f(n) // f(n - k) // f(k)


def count_combinations(n, m):
    return 2 ** n - sum([c(n, k) for k in range(0, m)])


max_exon_count, min_exon_count = 6, 3
res = count_combinations(max_exon_count, min_exon_count)
print(res % 1000000)
