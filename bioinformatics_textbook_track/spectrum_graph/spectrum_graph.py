from utils.constants import ACID_MASS

INT_MASS = {int(m): a for a, m in ACID_MASS.items()}
MAX_MASS = max(INT_MASS)


def spectrum_graph(s):
    graph = []
    for i in range(0, len(s)):
        j = i + 1
        while j < len(s) and s[j] - s[i] <= MAX_MASS:
            m = s[j] - s[i]
            if m in INT_MASS:
                graph.append((s[i], s[j], INT_MASS[m]))
            j += 1
    return graph


def stringify_graph(graph):
    return [f'{q}->{p}:{a}' for q, p, a in graph]


with open('spectrum.txt') as file:
    values = [0, *list(map(int, file.read().split()))]

    g = spectrum_graph(values)
    res = stringify_graph(g)
    print(*res, sep='\n')
