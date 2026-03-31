from utils.graphs import edge_list
import numpy as np
from numpy.typing import NDArray

L_MAX = 2 ** 31 - 1


def adjacency_matrix(e_list: list[tuple[int, int, int]], n: int) -> NDArray[np.float64]:
    a = np.full((n, n), np.inf)
    for u, v, l in e_list:
        a[u - 1, v - 1] = l
    for i in range(0, n):
        a[i, i] = 0
    return a


def dijkstra(a: NDArray[np.float64]) -> tuple[NDArray[np.int64], NDArray[np.int64]]:
    n, _ = a.shape
    l = np.full(n, L_MAX)
    l[0] = 0
    p = np.full(n, False)
    t = np.full(n, -1)

    while not p.all():
        i = np.where(p, np.inf, l).argmin()
        v = l[i] + a[i] < l
        l[v] = l[i] + a[i, v]
        t[v] = i
        p[i] = True
    return t, np.where(l == L_MAX, -1, l)


def main():
    with open('graph.txt') as file:
        n, _, e_list = edge_list(file)
        a = adjacency_matrix(e_list, n)
        _, l = dijkstra(a)
        np.savetxt('res.txt', l, fmt='%d', newline=' ')


if __name__ == '__main__':
    main()
