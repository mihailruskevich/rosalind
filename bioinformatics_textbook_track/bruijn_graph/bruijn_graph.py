
def create_graph(seq, k):
    mer_map = {}
    for i in range(0, len(seq) - k + 1):
        mer, next_mer = seq[i:i + k - 1], seq[i + 1:i + k]
        if mer in mer_map:
            mer_map[mer].append(next_mer)
        else:
            mer_map[mer] = [next_mer]
    return mer_map


def print_map(mer_map):
    for k, v in mer_map.items():
        print(k, '->', ','.join(v))


with open('data.txt') as file:
    length, dna = file.read().split()
    res = create_graph(dna, int(length))
    print_map(res)
