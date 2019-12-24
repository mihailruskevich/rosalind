from utils.common import reverse_complement

[seq] = open('dna.txt')
complement = reverse_complement(seq)
print(complement)