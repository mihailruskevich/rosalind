from utils.common import int_list


def partition(a, x):
    i, j = 0, len(a) - 1
    while i < j:
        while a[i] < x:
            i += 1
        while a[j] > x:
            j -= 1
        a[i], a[j] = a[j], a[i]


_, line = open('array.txt')
arr = int_list(line)
partition(arr, arr[0])

res = ' '.join(map(str, arr))
open('res.txt', 'w').write(res)
