from itertools import product


def states(p, p_alp):
    count_map = {}
    for v in zip(p, p[1:]):
        if v in count_map:
            count_map[v] += 1
        else:
            count_map[v] = 1
    for pair in product(path_alp, repeat=2):
        if pair not in count_map:
            count_map[pair] = 0
    return probability_map(count_map, p_alp)


def hmm(x, p, x_alp, p_alp):
    count_map = {}
    for v in zip(p, x):
        if v in count_map:
            count_map[v] += 1
        else:
            count_map[v] = 1
    for v in product(p_alp, x_alp):
        if v not in count_map:
            count_map[v] = 0
    return probability_map(count_map, p_alp)


def probability_map(count_map, p_alp):
    pr_map = {}
    for c in p_alp:
        s = sum(v for k, v in count_map.items() if k[0] == c)
        for k, v in count_map.items():
            if c == k[0]:
                if s != 0:
                    pr_map[k] = v / s
                else:
                    pr_map[k] = 1 / len(p_alp)
    return pr_map


def print_map(v_map, p_alp, x_alp):
    print('\t', end='')
    for c in x_alp:
        print(c, end='\t')
    print()
    for c in p_alp:
        print(c, end='\t')
        for v in x_alp:
            print(v_map[(c, v)], end='\t')
        print()


with open('data.txt') as file:
    lines = [p.split() for p in file.read().split('--------')]
    x_values, alp, path, path_alp = lines
    st_map = states(*path, path_alp)
    hmm_map = hmm(*x_values, *path, alp, path_alp)
    print_map(st_map, path_alp, path_alp)
    print('--------')
    print_map(hmm_map, path_alp, alp)
