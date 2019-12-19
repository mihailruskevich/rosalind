from math import factorial as f


def c(n, k):
    return f(n) // f(n - k) // f(k)


def belong_to_generation(k, n):
    m = 2 ** k
    return 1 - sum([c(m, i) * (1 / 4) ** i * (3 / 4) ** (m - i) for i in range(0, n)])


organisms_amount = 18
generation = 6
probability = belong_to_generation(generation, organisms_amount)
print(probability)
