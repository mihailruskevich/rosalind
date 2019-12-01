from utils.uni_prot import protein_sequence

compiled_motif = [
    lambda ch: ch == 'N',
    lambda ch: ch != 'P',
    lambda ch: ch in 'ST',
    lambda ch: ch != 'P'
]
motif_len = len(compiled_motif)


def matches(seq):
    return all(check(char) for check, char in zip(compiled_motif, seq))


def find_indices(seq):
    return [i + 1 for i in range(len(seq) - motif_len + 1) if matches(seq[i: i + motif_len])]


def find_motif(id_list):
    proteins = [(u_id, protein_sequence(u_id)) for u_id in id_list]
    return [(u_id, find_indices(seq)) for u_id, seq in proteins]


def print_results(proteins):
    for u_id, seq in proteins:
        if len(seq) != 0:
            print(u_id)
            print(' '.join(map(str, seq)))


file = open('proteins.txt')
ids = [v.rstrip() for v in file]
motifs = find_motif(ids)
print_results(motifs)
