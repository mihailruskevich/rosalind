from itertools import groupby


def fasta_sequences(fasta_file):
    groups = groupby(fasta_file, lambda line: line.startswith('>'))
    for _, grouper in groups:
        seq_id = next(grouper).strip('>\n')
        _, seq_array = next(groups)
        seq = ''.join([v.rstrip() for v in seq_array])
        yield seq_id, seq
