def group(p, i_list):
    m = {}
    for i, c in enumerate(p):
        if i in i_list and c != '-':
            if c in m:
                m[c].append(i)
            else:
                m[c] = [i]
    return m


def _create_trie(tuple_list, adj_list, i_list, v, level):
    if level < len(tuple_list):
        u = v[0]
        for c, indices in group(tuple_list[level], i_list).items():
            v[0] += 1
            adj_list.append((u, v[0], c))
            _create_trie(tuple_list, adj_list, indices, v, level + 1)


def create_trie(s_list):
    max_len = len(max(s_list, key=len))
    seq_list = map(lambda s: s.ljust(max_len, '-'), s_list)
    adj_list, i_list = [], list(range(0, len(s_list)))
    _create_trie(list(zip(*seq_list)), adj_list, i_list, [1], 0)
    return adj_list


def write_result(adj_list, file):
    for e in adj_list:
        file.write(' '.join(map(str, e)) + '\n')


with open('seq.txt') as seq_file, open('res.txt', 'w') as res_file:
    dna_list = seq_file.read().split()
    adjacency_list = create_trie(dna_list)
    write_result(adjacency_list, res_file)
