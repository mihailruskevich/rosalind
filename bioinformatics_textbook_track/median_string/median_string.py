def hamming(p, line, i):
    h = 0
    for index in range(0, len(p)):
        if p[index] != line[index + i]:
            h += 1
    return h


def d_line(p, line):
    min_d = len(p)
    for i in range(0, len(line) - len(p) + 1):
        d = hamming(p, line, i)
        if d == 0:
            return 0
        elif d < min_d:
            min_d = d
    return min_d


def median_string(k, dna_list):
    [first, *rest] = dna_list
    median, min_sum = "", k * len(dna_list)
    for i in range(0, len(first) - k + 1):
        p = first[i: i + k]
        d_sum = sum(d_line(p, line) for line in rest)
        if d_sum < min_sum:
            min_sum, median = d_sum, p
    return median


with open('data.txt') as file:
    [length, *lines] = file.read().split()
    res = median_string(int(length), lines)
    print(res)
