from itertools import product

from utils.arrays import stringify


def k_mer_list(k):
    return map(''.join, product('ACGT', repeat=k))


def count_matches(seq, k_mer):
    i, count = seq.find(k_mer), 0
    while i != -1:
        i = seq.find(k_mer, i + 1)
        count += 1
    return count


def frequency_array(seq, k):
    return [count_matches(seq, mer) for mer in k_mer_list(k)]


with open('data.txt') as file, open('res.txt', 'w') as res_file:
    dna, length = file.read().split()
    res = frequency_array(dna, int(length))
    res_file.write(stringify(res))
