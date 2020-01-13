from utils.common import int_list


def search(a, x, i, key):
    j = len(a) - 1
    mid = j
    while key(a[mid]) != x and i < j:
        i, j = (mid + 1, j) if key(a[mid]) < x else (i, mid)
        mid = (i + j) // 2
    return mid if key(a[mid]) == x else -1


def distinct(e):
    return list({v[1]: v for v in e}.values())


def zero_third(a):
    a = sorted(distinct(enumerate(a)), key=lambda v: v[1])
    for p in range(0, len(a)):
        for q in range(p + 1, len(a)):
            r = a[p][1] + a[q][1]
            k = search(a, -r, q + 1, lambda v: v[1])
            if k != -1:
                return sorted([a[p][0], a[q][0], a[k][0]])
    return -1, -1, -1


def print_arrays(array_list):
    for p, q, r in map(zero_third, array_list):
        print(p if p == -1 else f'{p + 1} {q + 1} {r + 1}')


_, *lines = open('arrays.txt')
arrays = [int_list(line.rstrip()) for line in lines]
print_arrays(arrays)
