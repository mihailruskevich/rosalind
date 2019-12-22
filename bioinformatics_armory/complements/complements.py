from Bio import SeqIO


def find_reverse_palindromes(seq_list):
    return [s.seq for s in seq_list if s.seq == s.reverse_complement().seq]


dna_list = SeqIO.parse(open('dna.fas'), 'fasta')
palindromes = find_reverse_palindromes(dna_list)
print(len(palindromes))
