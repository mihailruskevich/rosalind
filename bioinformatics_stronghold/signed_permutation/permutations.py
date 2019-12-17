def permutations(a, index, res):
    if index < len(a):
        i = index
        while i < len(a):
            b = a.copy()
            b[index], b[i] = b[i], b[index]
            i = i + 1
            permutations(b, index + 1, res)
    else:
        res.append(a)


def signed_combinations(p, index, res):
    if index < len(p):
        k = p.copy()
        k[index] *= -1
        signed_combinations(p, index + 1, res)
        signed_combinations(k, index + 1, res)
    else:
        res.append(p)


def signed_permutations(n):
    values = list(range(1, n + 1))
    res = []
    permutations(values, 0, res)
    total = []
    for p in res:
        signed_p = []
        signed_combinations(p, 0, signed_p)
        total.extend(signed_p)
    return total


def print_result(values):
    print(len(values))
    for v in values:
        print(*v)


length = 5
signed_values = signed_permutations(length)
print_result(signed_values)
