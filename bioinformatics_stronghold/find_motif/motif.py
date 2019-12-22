
def motif_indices(seq, t):
    return [i + 1 for i in range(0, len(seq) - len(t) + 1) if seq[i:i + len(t)] == t]


dna, motif = open('dna_motif.txt')
nums = motif_indices(dna, motif)
print(' '.join(map(str, nums)))
