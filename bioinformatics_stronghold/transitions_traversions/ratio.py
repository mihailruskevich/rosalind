from utils.fasta import fasta_sequences


def is_transition(p):
    return 'A' in p and 'G' in p or \
           'C' in p and 'T' in p


def category(p):
    return 3 if p[0] == p[1] else 1 if is_transition(p) else 2


def ratio(s1, s2):
    categories = list(map(lambda p: category(p), zip(s1, s2)))
    return categories.count(1) / categories.count(2)


(_, seq_a), (_, seq_b) = fasta_sequences(open('dna.fas'))
res = ratio(seq_a, seq_b)
print(res)
