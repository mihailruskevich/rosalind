from utils.common import int_list


def equality_partition(a, x, i):
    j = len(a) - 1
    while i < j:
        while a[i] == x:
            i += 1
        while a[j] != x:
            j -= 1
        if i < j:
            a[i], a[j] = a[j], a[i]


def partition(a, x):
    i, j = 0, len(a) - 1
    while i < j:
        while a[i] < x:
            i += 1
        while a[j] >= x:
            j -= 1
        if i < j:
            a[i], a[j] = a[j], a[i]
    return i


def three_way_partition(a, x):
    i = partition(a, x)
    equality_partition(a, x, i)


_, line = open('array.txt')
arr = int_list(line)

three_way_partition(arr, arr[0])
res = ' '.join(map(str, arr))
open('res.txt', 'w').write(res)
