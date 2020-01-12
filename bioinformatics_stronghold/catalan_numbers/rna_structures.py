from utils.fasta import fasta_sequences


# example of catalan numbers calculation(not related to task)
def check_map(n, c_map):
    if n not in c_map:
        c_map[n] = _cat(n, c_map)
    return c_map[n]


def _cat(n, c_map):
    return sum(check_map(k - 1, c_map) * check_map(n - k, c_map) for k in range(1, n + 1))


def cat(n):
    return _cat(n, {0: 1, 1: 1})


COMPLEMENT = {
    'A': 'U',
    'C': 'G',
    'G': 'C',
    'U': 'A'
}


def check_fragment(s, i, j):
    return s.count('A', i, j) == s.count('U', i, j) and s.count('C', i, j) == s.count('G', i, j)


def c_cache(s, i, j, s_map):
    if (i, j) not in s_map:
        s_map[(i, j)] = c(s, i, j, s_map)
    return s_map[(i, j)]


def c(s, i, j, s_map):
    if j - i <= 1:
        return 1
    count, index = 0, i
    while True:
        index = s.find(COMPLEMENT[s[i]], index + 1, j)
        if index == -1:
            break
        if not check_fragment(s, i + 1, index):
            continue
        count += c_cache(s, i + 1, index, s_map) * c_cache(s, index + 1, j, s_map)
    return count


with open('rna.fas') as file:
    [(_, rna)] = fasta_sequences(file)
    non_crossing_perfect_matching_count = c(rna, 0, len(rna), {})
    print(non_crossing_perfect_matching_count)
    print(non_crossing_perfect_matching_count % 1000000)
