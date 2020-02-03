from utils.constants import RNA_CODES


def translate(seq):
    acids = [RNA_CODES[seq[i:i + 3]] for i in range(0, len(seq) - 2, 3)]
    return acids[0: acids.index('Stop')]


with open('dna.txt') as [dna]:
    acid_list = translate(dna)
    res = ''.join(acid_list)
    print(res)
