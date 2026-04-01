from utils.common import reverse_complement_2


def bruijn_graph(dna_list: list[str]) -> list[tuple[str, str]]:
    k = len(dna_list[0]) - 1
    s = set(dna_list)
    s_rc = {reverse_complement_2(d) for d in s}
    return [(d[0: k], d[1: k + 1]) for d in s | s_rc]


def main():
    with open('data.txt', 'r') as file, open('res.txt', 'w') as res_file:
        graph = bruijn_graph(file.read().splitlines())
        res_file.write('\n'.join([f'({u}, {v})' for u, v in graph]))


if __name__ == '__main__':
    main()
