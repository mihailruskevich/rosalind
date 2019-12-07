from utils.graphs import degree_list, edge_list

file = open('graph.txt')
v_count, _, graph = edge_list(file)
degree_values = degree_list(graph, v_count)
print(*degree_values)
