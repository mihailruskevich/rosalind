from math import log10 as lg
from math import factorial as f


def c(n, k):
    return f(n) // f(n - k) // f(k)


def sharing_chromosomes(n, k):
    return lg(sum(c(n, i) for i in range(k, n + 1))) - (n * lg(2))


def probability_range(n):
    return [sharing_chromosomes(2 * n, k) for k in range(1, 2 * n + 1)]


chromosomes_count = 46
res = probability_range(chromosomes_count)
print(*res)
