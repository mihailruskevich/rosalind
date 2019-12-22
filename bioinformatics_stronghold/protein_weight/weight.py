from functools import reduce

from utils.constants import ACID_MASS


def weight(protein):
    return reduce(lambda mass, acid: mass + ACID_MASS[acid], protein, 0)


acids = open('prot.txt').readline()
protein_weight = weight(acids)
print(protein_weight)
