from utils.common import reverse_complement
from utils.constants import RNA_CODES
from utils.fasta import fasta_sequences

ACID_LEN = 3


def translate(rna):
    return [RNA_CODES[rna[i:i + ACID_LEN]] for i in range(0, len(rna) - ACID_LEN + 1, ACID_LEN)]


def find_orf(acid_list):
    index = 0
    frames = []
    while index < len(acid_list):
        try:
            start_index = acid_list.index('M', index, len(acid_list))
            stop_index = acid_list.index('Stop', start_index + 1, len(acid_list))
            frames.append(''.join(acid_list[start_index: stop_index]))  # no need +1 since last is Stop codon
            index = start_index + 1
        except ValueError:
            break
    return frames


def reading_frames(dna):
    rna = dna.replace('T', 'U')
    r_rna = reverse_complement(dna).replace('T', 'U')
    return [
        rna, r_rna,
        rna[1:], r_rna[1:],
        rna[2:], r_rna[2:]
    ]


def all_proteins(dna):
    frames = reading_frames(dna)
    translated_frames = [translate(f) for f in frames]
    orf_proteins = [find_orf(tf) for tf in translated_frames]
    return [p for proteins in orf_proteins for p in proteins]


file = open('dna.fas')
_key, dna_seq = next(fasta_sequences(file))
result_proteins = all_proteins(dna_seq)

for pr in set(result_proteins):
    print(pr)
