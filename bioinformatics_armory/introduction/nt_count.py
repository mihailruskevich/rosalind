from Bio.Seq import Seq

line = open('dna.txt').read()
seq = Seq(line)
nt_count = list(map(seq.count, 'ACGT'))
print(*nt_count)
