
def edge_list(lines):
    (v_count, e_count), *graph = [tuple(map(int, pair.rstrip().split(' '))) for pair in lines]
    return v_count, e_count, graph


def degree_list(edges, n):
    d = [0] * n
    for u, v in edges:
        d[u - 1] += 1
        d[v - 1] += 1
    return d


def adjacency_list(edges, n):
    a = [[] for _ in range(n)]
    for u, v in edges:
        a[u - 1].append(v)
        a[v - 1].append(u)
    return a
