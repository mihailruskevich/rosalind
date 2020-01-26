def matches(s, p, d, i):
    return len([1 for x, y in zip(s[i: i + len(p)], p) if x != y]) <= d


def find_matches(s, p, d):
    return [i for i in range(0, len(s) - len(p) + 1) if matches(s, p, d, i)]


with open('data.txt') as file:
    pattern, dna, mismatches = file.read().split()
    res = find_matches(dna, pattern, int(mismatches))
    print(*res)
