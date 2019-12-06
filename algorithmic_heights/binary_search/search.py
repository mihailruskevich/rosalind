from utils.common import int_list


def search(a, x):
    i, j = 0, len(a) - 1
    mid = j // 2
    while a[mid] != x and i < j:
        i, j = (mid + 1, j) if a[mid] < x else (i, mid)
        mid = (i + j) // 2
    return mid if a[mid] == x else -2


def search_values(a, b):
    cache, res = {}, []
    for x in b:
        if x not in cache:
            cache[x] = search(a, x)
        res.append(cache[x])
    return res


def stringify_result(a):
    return ' '.join(map(lambda v: str(v + 1), a))


arr1, arr2 = open('values.txt')
ordered = int_list(arr1)
values = int_list(arr2)

indices = stringify_result(search_values(ordered, values))
open('res.txt', 'w').write(indices)
