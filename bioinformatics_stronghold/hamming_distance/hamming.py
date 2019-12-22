
def d(l_seq, r_seq):
    return len([bp for bp in zip(l_seq, r_seq) if bp[0] != bp[1]])


file = open('dna_2.txt')
l_s = file.readline()
r_s = file.readline()
hamming = d(l_s, r_s)

print(hamming)
