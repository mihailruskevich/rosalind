import time

from utils.fasta import fasta_sequences


def shared_motif(sequences):
    curr_max = 0
    curr_max_seq = ''
    seq_a = sequences[0]
    tail = sequences[1:]
    for i in range(len(seq_a) - 1):
        for j in range(2, len(seq_a) - i):
            curr_seq = seq_a[i:i + j]
            match_count = 0
            for seq in tail:
                if curr_seq in seq:
                    match_count += 1
                else:
                    break
            if match_count == len(tail) and j > curr_max:
                curr_max, curr_max_seq = j, curr_seq
    return curr_max_seq


fas_sequences = [seq for key, seq in fasta_sequences(open('dna.fas'))]
start_time = time.time()
motif = shared_motif(sorted(fas_sequences))
print(f'Execution time: {time.time() - start_time} seconds')
print(motif)
