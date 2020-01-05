from Bio import SeqIO


def trim_record(s, threshold):
    bases_q = s.letter_annotations['phred_quality']
    i, j = 0, len(bases_q) - 1
    while i < len(bases_q) and bases_q[i] < threshold:
        i += 1
    while j > i and bases_q[j] < threshold:
        j -= 1
    return s[i: j + 1]


def trim_by_quality(seq_list, threshold):
    return (trim_record(s, threshold) for s in seq_list)


with open('dna.fq') as dna_file, open('trimmed.fq', 'w') as res_file:
    quality_threshold = 20
    dna_list = SeqIO.parse(dna_file, 'fastq')
    trimmed_list = trim_by_quality(dna_list, quality_threshold)
    SeqIO.write(trimmed_list, res_file, 'fastq')
