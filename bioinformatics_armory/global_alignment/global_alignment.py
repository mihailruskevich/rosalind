from Bio import Entrez, SeqIO
from Bio import pairwise2

FAS = 'fasta'
Entrez.email = "no_warning@mail.com"


# Scores used from task description.
# Gap opening penalty of 10.
# Gap extension penalty of 1.
# Matches and mismatches used from shared matrix(5, -4)
def max_score(id_list):
    seq_handle = Entrez.efetch(db='nucleotide', id=id_list, rettype=FAS)
    seq_1, seq_2 = map(lambda s: s.seq, SeqIO.parse(seq_handle, FAS))
    first_alignment = pairwise2.align.globalms(seq_1, seq_2, 5, -4, -10, -1)[0]
    return first_alignment[2]


ids = 'JQ712977.1 JX308819.1'.split()
score = max_score(ids)
print(int(score))
