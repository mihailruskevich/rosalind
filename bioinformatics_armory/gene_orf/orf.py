from Bio.Seq import Seq


def reading_frames(dna):
    seq = Seq(dna)
    r_seq = seq.reverse_complement()
    return [
        seq, r_seq,
        seq[1:-2], r_seq[1:-2],
        seq[2:-1], r_seq[2:-1]
    ]


def find_orf(seq):
    index, frames = 0, []
    p = seq.translate()
    while index < len(p):
        try:
            start_index = p.index('M', index)
            stop_index = p.index('*', start_index + 1)
            frames.append(p[start_index: stop_index])
            index = start_index + 1
        except ValueError:
            break
    return frames


def longest_protein(dna):
    seq_list = reading_frames(dna)
    orf_list = [p for s in seq_list for p in find_orf(s)]
    return max(orf_list, key=len)


with open('dna.txt') as [sequence]:
    res = longest_protein(sequence)
    print(res)
