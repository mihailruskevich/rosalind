from random import randint

from utils.arrays import equality_partition
from utils.common import int_list


def partition(a, x, i, j):
    while i < j:
        while a[i] < x:
            i += 1
        while j >= 0 and a[j] >= x:
            j -= 1
        if i < j:
            a[i], a[j] = a[j], a[i]
    return i


def three_way_partition(a, x, i, j):
    mid_st = partition(a, x, i, j)
    r_st = equality_partition(a, x, mid_st, j)
    return mid_st, r_st


def select(a, k, i, j):
    x = a[randint(i, j)]
    mid_st, r_st = three_way_partition(a, x, i, j)
    if mid_st <= k < r_st or mid_st == k:
        return x
    elif k < mid_st:
        return select(a, k, i, mid_st - 1)
    else:
        return select(a, k, r_st, j)


_, line1, line2 = open('array.txt')
arr = int_list(line1)
position = int(line2) - 1

k_element = select(arr, position, 0, len(arr) - 1)
print(k_element)
