import numpy as np
from Bio import SeqIO


def count_below(seq_list, threshold):
    quality_matrix = np.array([s.letter_annotations['phred_quality'] for s in seq_list])
    return (np.mean(quality_matrix, axis=0) < threshold).sum()


with open('dna.fq') as dna_file:
    quality_threshold = 26
    dna_list = SeqIO.parse(dna_file, 'fastq')
    poor_quality_bases = count_below(dna_list, quality_threshold)
    print(poor_quality_bases)
