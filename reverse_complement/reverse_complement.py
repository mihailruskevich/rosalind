COMPLEMENT = {
    'A': 'T',
    'C': 'G',
    'G': 'C',
    'T': 'A'
}


def reverse_complement(dna):
    return [COMPLEMENT[nt] for nt in dna[::-1]]


seq = open('rosalind_dna.txt', 'r').read()
reversed_seq = ''.join(reverse_complement(seq))
open('rosalind_result.txt', 'w').write(reversed_seq)
