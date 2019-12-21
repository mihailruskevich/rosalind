from utils.fasta import fasta_sequences


def find_spliced_motif(s, t):
    indices, i = [], -1
    for nt in t:
        i = s.find(nt, i + 1)
        indices.append(i)
    return indices


(_, dna), (_, motif) = fasta_sequences(open('dna.fas'))
res = find_spliced_motif(dna, motif)
print(*map(lambda i: i + 1, res))
