from utils.graphs import edge_list, adjacency_list


def visit(a_list, curr_v, visited):
    visited[curr_v - 1] = True
    for v in a_list[curr_v - 1]:
        if not visited[v - 1]:
            visit(a_list, v, visited)


def count_components(edges, n):
    visited = [False] * v_count
    a_list = adjacency_list(edges, n)
    components_count = 0
    while not all(visited):
        curr_v = visited.index(False) + 1
        visit(a_list, curr_v, visited)
        components_count += 1
    return components_count


with open('graph.txt') as file:
    v_count, _, edge_list = edge_list(file)
    res = count_components(edge_list, v_count)
    print(res)
