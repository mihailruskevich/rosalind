
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


def print_permutations(perm_list):
    for p in perm_list:
        print(' '.join(map(str, p)))


n = 5
values = list(range(1, n + 1))
permutations_list = []
permutations(values, 0, permutations_list)

print(len(permutations_list))
print_permutations(permutations_list)
