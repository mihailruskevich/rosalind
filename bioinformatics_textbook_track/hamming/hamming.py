from utils.common import hamming

a, b = open('dna.txt').read().split()
print(hamming(a, b))
