from utils.constants import ACID_MASS

INT_MASS = {a: int(m) for a, m in ACID_MASS.items()}


def peptide_vector(p):
    v = [0] * sum(INT_MASS[a] for a in p)
    mass = 0
    for a in p:
        mass += INT_MASS[a]
        v[mass - 1] = 1
    return v


with open('peptide.txt') as file:
    peptide = file.read()
    res = peptide_vector(peptide)
    print(*res)
