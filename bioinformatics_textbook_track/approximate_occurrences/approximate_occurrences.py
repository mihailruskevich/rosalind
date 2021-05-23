import itertools


# implementation which worked more than 5 minutes
def find_occurrences(dna, patterns, d):
    return [i for j in range(0, len(patterns)) for i in range(0, len(dna) - len(patterns[j]) + 1) if
            sum(1 for x, y in zip(dna[i: i + len(patterns[j])], patterns[j]) if x != y) <= d]


def matches(dna, p, i, d):
    j, mismatches = 0, 0
    while j < len(p) and mismatches <= d:
        if dna[i + j] != p[j]:
            mismatches += 1
        j += 1
    return mismatches <= d


def find_occurrences_2(dna, patterns, d):
    return [i for j in range(0, len(patterns)) for i in range(0, len(dna) - len(patterns[j]) + 1) if
            matches(dna, patterns[j], i, d)]


# implementation which functions
def find_occurrences_3(dna, patterns, d):
    return itertools.chain(
        *map(lambda j: filter(lambda i: matches(dna, patterns[j], i, d), range(0, len(dna) - len(patterns[j]) + 1)),
             range(0, len(patterns)))
    )


with open('data.txt') as file:
    [line, pattern_list, value] = map(str.strip, file.readlines())
    print(*find_occurrences_2(line, pattern_list.split(), int(value)))
