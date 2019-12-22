from utils.fasta import fasta_sequences

INDICES = {
    'A': 0,
    'C': 1,
    'G': 2,
    'T': 3
}
NT_ARRAY = 'ACGT'


def create_profile(dna_lines):
    profile = [[0 for _ in range(len(dna_lines[0]))] for _ in range(4)]
    for seq in dna_lines:
        for i, nt in enumerate(seq):
            profile[INDICES[nt]][i] += 1
    return profile


def consensus(profile):
    consensus_st = ''
    for j in range(len(profile[0])):
        p_column = [p_line[j] for p_line in profile]
        nt_index, _ = max(enumerate(p_column), key=lambda pair: pair[1])
        consensus_st += NT_ARRAY[nt_index]
    return consensus_st


file = open('dna.fas')
sequences = [seq for key, seq in fasta_sequences(file)]
dna_profile = create_profile(sequences)
consensus_value = consensus(dna_profile)

print('   ' + ' '.join(consensus_value))
for i, line in enumerate(dna_profile):
    print('{}: {}'.format(NT_ARRAY[i], ' '.join(map(str, line))))
