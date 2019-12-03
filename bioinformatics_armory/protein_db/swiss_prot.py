from Bio import ExPASy
from Bio import SwissProt


def extract_processes(protein):
    return [ref[2].replace('P:', '') for ref in protein.cross_references if ref[0] == 'GO' and ref[2].startswith('P:')]


uniprot_id = 'A1JJT5'
txt_handle = ExPASy.get_sprot_raw(uniprot_id)
swiss_prot = SwissProt.read(txt_handle)
processes = extract_processes(swiss_prot)
print(*processes, sep='\n')
