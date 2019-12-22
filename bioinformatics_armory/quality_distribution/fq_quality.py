from statistics import mean

from Bio import SeqIO


def find_below(seq_list, threshold):
    return [s for s in seq_list if mean(s.letter_annotations['phred_quality']) < threshold]


quality_threshold = 28
dna_list = SeqIO.parse(open('dna.fq'), 'fastq')
poor_quality_list = find_below(dna_list, quality_threshold)
print(len(poor_quality_list))
