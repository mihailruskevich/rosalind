def k_mer_map(seq, k):
    k_map = {}
    for i, k_mer in enumerate([seq[i:i + k] for i in range(0, len(seq) - k + 1)]):
        if k_mer in k_map:
            k_map[k_mer].append(i)
        else:
            k_map[k_mer] = [i]
    return k_map


def check_range(i_list, r, k):
    return i_list[-1] - i_list[0] + k <= r


def clumps(seq, k, t, r):
    # return [k_mer for k_mer, i_list in k_mer_map(seq, k).items() if len(i_list) >= t and check_range(i_list, r, k)]
    return [k_mer for k_mer, i_list in k_mer_map(seq, k).items() if len(i_list) >= t]


with open('data.txt') as file:
    dna, length, interval, matches_count = file.read().split()
    length, interval, matches_count = map(int, [length, interval, matches_count])
    res = clumps(dna, length, matches_count, interval)
    print(*res)
