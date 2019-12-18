from utils.fasta import fasta_sequences


def overlap_graph(sequences, k):
    pairs = []
    for key_v, seq_v in sequences:
        for key_w, seq_w in sequences:
            if seq_v != seq_w and seq_v[len(seq_v) - k: len(seq_v)] == seq_w[0: k]:
                pairs.append((key_v, key_w))
    return pairs


k_val = 3
fas_sequences = list(fasta_sequences(open('dna.fas')))
adjacency_list = overlap_graph(fas_sequences, k_val)
print(*map(' '.join, adjacency_list), sep='\n')
