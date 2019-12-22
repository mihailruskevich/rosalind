from Bio import Entrez
from Bio import SeqIO

FAS = 'fasta'
Entrez.email = "no_warning@mail.com"


def find_shortest(id_list):
    seq_handle = Entrez.efetch(db='nucleotide', id=id_list, rettype=FAS)
    return min(SeqIO.parse(seq_handle, FAS), key=lambda record: len(record.seq))


fasta_id_list = next(open('gen_bank_ids.txt')).split()
seq_record = find_shortest(fasta_id_list)
print(seq_record.format(FAS))
