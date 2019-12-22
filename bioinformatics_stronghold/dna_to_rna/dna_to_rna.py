
def transcribe(dna):
    return dna.replace('T', 'U')


seq = open('rosalind_dna.txt', 'r').read()
rna = transcribe(seq)
open('rosalind_result.txt', 'w').write(rna)
