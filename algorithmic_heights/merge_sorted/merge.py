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


def merge(a, b):
    i, j, c = 0, 0, []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    c += a[i:] if i < len(a) else b[j:]
    return c


_, line1, _, line2 = open('arrays.txt')
arr1, arr2 = int_list(line1), int_list(line2)

merged = merge(arr1, arr2)
print(*merged)
