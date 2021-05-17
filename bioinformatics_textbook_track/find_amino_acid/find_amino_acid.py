import itertools
import re

from utils.common import reverse_complement_2
from utils.constants import RNA_CODES


def acid_codes():
    a_codes = {}
    for c, a in RNA_CODES.items():
        if a in a_codes:
            a_codes[a].add(c)
        else:
            a_codes[a] = {c}
    return a_codes


def prot_to_rna(p):
    codes = acid_codes()
    p_as_rna = itertools.product(*map(lambda a: codes[a], p))
    return map(''.join, p_as_rna)


def find_amino_acid(dna, p):
    rev_rna = reverse_complement_2(dna).replace('T', 'U')
    rna = dna.replace('T', 'U')
    prot_codes = prot_to_rna(p)

    dna_list = []
    for p_code in prot_codes:
        dna_list.extend(map(lambda m: dna[m.start(): m.end()], re.finditer(p_code, rna)))
        dna_list.extend(map(lambda m: dna[len(dna) - m.end(): len(dna) - m.start()], re.finditer(p_code, rev_rna)))
    return dna_list


with open('data.txt') as file:
    (line, prot) = map(str.strip, file.readlines())
    res = find_amino_acid(line, prot)
    print(*res, sep='\n')
