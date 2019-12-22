from Bio import SeqIO

seq_list = SeqIO.parse(open('dna.fq'), 'fastq')
for seq in seq_list:
    print(seq.format('fasta'))
