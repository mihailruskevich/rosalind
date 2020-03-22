from utils.fasta import fasta_sequences


def starts(s1, s2):
    for j in range(0, len(s1) // 2):
        if s2.startswith(s1[j:]):
            return j
    return -1


def ends(s1, s2):
    for j in range(len(s1), len(s1) // 2, -1):
        if s2.endswith(s1[0:j]):
            return j
    return -1


def super_string(s_list):
    [sup, *rest] = s_list
    while len(rest) > 0:
        for s in rest:
            i = starts(s, sup)
            if i != -1:
                sup = s[0:i] + sup
                rest.remove(s)
            else:
                j = ends(s, sup)
                if j != - 1:
                    sup += s[j:]
                    rest.remove(s)
    return sup


with open('dna.fas') as dna_file:
    sequences = [seq for _, seq in fasta_sequences(dna_file)]
    res = super_string(sequences)
    print(res)
