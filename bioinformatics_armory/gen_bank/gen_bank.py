from Bio import Entrez

genus_name = 'Xenolophium'
start_date = '2000/09/26'
end_date = '2012/02/26'

search_term = '"{}"[Organism] AND ("{}"[PDAT] : "{}"[PDAT])'.format(genus_name, start_date, end_date)
handle = Entrez.esearch(db='nucleotide', term=search_term)
result = Entrez.read(handle)
print(result['Count'])
