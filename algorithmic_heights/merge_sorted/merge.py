from utils.arrays import merge
from utils.common import int_list


# Recursion implementation. Works only for small data sets.
# Parameter `c` needed for storing result.
def merge_lists(a, b, c):
    if len(a) and len(b):
        ls, gt = (a, b) if a[0] < b[0] else (b, a)
        c.append(ls[0])
        merge_lists(ls[1:], gt, c)
    else:
        c += a if len(a) else b


_, line1, _, line2 = open('arrays.txt')
arr1, arr2 = int_list(line1), int_list(line2)

merged = merge(arr1, arr2)
print(*merged)
