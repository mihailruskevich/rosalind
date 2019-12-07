from utils.graphs import adjacency_list, degree_list, edge_list


def double_degree_list(edges, n):
    d_list = degree_list(edges, n)
    a_list = adjacency_list(edges, n)
    return [sum(map(lambda v: d_list[v - 1], v_list)) for v_list in a_list]


with open('graph.txt') as edges_file:
    v_count, _, graph = edge_list(edges_file)
    dd_list = double_degree_list(graph, v_count)
    print(*dd_list)
