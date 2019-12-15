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


def partition(a, x, i, j):
    while i < j:
        while a[i] < x:
            i += 1
        while a[j] >= x:
            j -= 1
        if i < j:
            a[i], a[j] = a[j], a[i]
    return i


def equality_partition(a, x, i, j):
    while i < j:
        while a[i] == x:
            i += 1
        while a[j] != x:
            j -= 1
        if i < j:
            a[i], a[j] = a[j], a[i]
    return i
