
def composition(seq, k):
    print(seq, k)
    return [seq[i:i + k] for i in range(0, len(seq) - k + 1)]


with open('data.txt') as file, open('res.txt', 'w') as res_file:
    length, dna = file.read().split()
    res = composition(dna, int(length))
    res_file.write('\n'.join(res))
