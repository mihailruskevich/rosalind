
def edge_list(lines):
    return [tuple(map(int, pair.rstrip().split(' '))) for pair in lines]


def degree_list(edges, n):
    d = [0] * n
    for u, v in edges:
        d[u - 1] += 1
        d[v - 1] += 1
    return d


file = open('graph.txt')
(v_count, e_count), *graph = edge_list(file)
degree_values = degree_list(graph, v_count)
print(*degree_values)
