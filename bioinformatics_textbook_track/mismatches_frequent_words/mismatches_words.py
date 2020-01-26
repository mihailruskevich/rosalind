from itertools import product


def k_mer_list(k):
    return map(''.join, product('ACGT', repeat=k))


def matches(s, mer, d, i):
    return len([1 for x, y in zip(s[i: i + len(mer)], mer) if x != y]) <= d


def matches_map(s, k, d):
    k_mers = k_mer_list(k)
    count_map = {}
    for k_mer in k_mers:
        for i in range(0, len(s) - k + 1):
            if matches(s, k_mer, d, i):
                if k_mer in count_map:
                    count_map[k_mer] += 1
                else:
                    count_map[k_mer] = 1
    return count_map


def find_frequent_k_mer_list(s, k, d):
    count_map = matches_map(s, k, d)
    max_match = max(count_map.values())
    return [k_mer for k_mer, m_count in count_map.items() if m_count == max_match]


with open('data.txt') as file:
    dna, length, mismatches = file.read().split()
    res = find_frequent_k_mer_list(dna, int(length), int(mismatches))
    print(*res)
