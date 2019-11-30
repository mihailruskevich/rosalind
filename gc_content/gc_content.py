from utils.common import gc_content
from utils.fasta import fasta_sequences


def sequences_gc(sequences):
    return [(seq_key, gc_content(dna)) for seq_key, dna in sequences]


file = open('dna.fas')
cg_map = sequences_gc(fasta_sequences(file))
max_gc = max(cg_map, key=lambda pair: pair[1])
file.close()

print(max_gc[0])
print(max_gc[1] * 100)
