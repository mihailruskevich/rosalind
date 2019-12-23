
def tree_missing_edges(lines):
    n, *graph_lines = lines
    return int(n) - len(graph_lines) - 1


file = open('graph.txt')
edges_count = tree_missing_edges(file)
print(edges_count)
