from requests import get

PROTEIN_PATH = 'http://www.uniprot.org/uniprot/{}.fasta'


def protein_sequence(protein_id):
    response = get(PROTEIN_PATH.format(protein_id))
    if response.status_code == 200:
        return ''.join(response.text.split('\n')[1:-1])
    else:
        raise Exception('Uniprot with id [{}] not found'.format(protein_id))
