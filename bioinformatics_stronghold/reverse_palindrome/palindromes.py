from utils.common import reverse_complement
from utils.fasta import fasta_sequences


def is_palindrome(seq):
    half = len(seq) // 2
    return reverse_complement(seq[:half]) == seq[half:]


def find_palindromes(seq):
    palindromes = []
    for line_len in range(4, 12 + 1, 2):
        for i in range(0, len(seq) - line_len + 1):
            if is_palindrome(seq[i:i + line_len]):
                palindromes.append((i + 1, line_len))
    return palindromes


file = open('dna.fas')
_key, dna = next(fasta_sequences(file))
palindrome_list = find_palindromes(dna)

for p in palindrome_list:
    print(' '.join(map(str, p)))
