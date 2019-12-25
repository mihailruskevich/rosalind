from utils.graphs import edge_list


# Default recursion depth allows only to use iterative approach
def _breadth_first_search(edges, curr_v, level, d):
    for u, v in edges:
        if u == curr_v:
            d[v - 1] = level
            _breadth_first_search(edges, v, level + 1, d)


def breadth_first_search(edges, n):
    d = [0] + [-1] * (n - 1)
    _breadth_first_search(edges, 1, 1, d)
    return d


def adjacency_list(edges, n):
    a = [[] for _ in range(n)]
    for u, v in edges:
        a[u - 1].append(v)
    return a


def breadth_first_search_queue(edges, n):
    a_list = adjacency_list(edges, n)
    visited = [True] + [False] * (n - 1)
    d = [0] + [-1] * (n - 1)
    q = [1]
    while q:
        curr_v = q.pop(0)
        for v in a_list[curr_v - 1]:
            if not visited[v - 1]:
                q.append(v)
                d[v - 1] = d[curr_v - 1] + 1
                visited[v - 1] = True
    return d


with open('graph.txt') as file, open('res.txt', 'w') as res_file:
    v_count, _, graph = edge_list(file)
    dist_list = breadth_first_search_queue(graph, v_count)
    res = ' '.join(map(str, dist_list))
    res_file.write(res)
