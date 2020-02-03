
def genome_path(seq_list):
    return seq_list[0] + ''.join([s[-1] for s in seq_list[1:]])


with open('dna.txt') as file:
    lines = file.read().split()
    res = genome_path(lines)
    print(res)
