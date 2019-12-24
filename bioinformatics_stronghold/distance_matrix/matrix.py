from Bio import SeqIO
from utils.common import hamming as d


def create_matrix(seq_list):
    n = len(seq_list[0])
    return [[d(s1, s2) / n for s2 in seq_list] for s1 in seq_list]


dna_list = [str(s.seq) for s in SeqIO.parse(open('dna.fas'), 'fasta')]
d_matrix = create_matrix(dna_list)

for line in d_matrix:
    print(*line)
