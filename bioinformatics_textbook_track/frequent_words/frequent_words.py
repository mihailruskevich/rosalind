def count_mer(seq, k):
    count_map = {}
    for i in range(0, len(seq) - k + 1):
        mer = seq[i:i + k]
        if mer in count_map:
            count_map[mer] += 1
        else:
            count_map[mer] = 1
    return count_map


def frequent_mer(seq, k):
    count_map = count_mer(seq, k)
    max_len = max(count_map.values())
    return [s for s, c in count_map.items() if c == max_len]


with open('dna.txt') as (dna, length):
    dna, length = dna.rstrip(), int(length)
    res = frequent_mer(dna, length)
    print(*res)
