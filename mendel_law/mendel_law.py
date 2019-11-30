# k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive
# k = B
# m = Bb
# n = b


def probability(k, m, n):
    total = m + n + k
    rec_mm = 0.25 * (m * (m - 1)) / (total * (total - 1))
    rec_nn = (n * (n - 1)) / (total * (total - 1))
    rec_nm = (n * m) / (total * (total - 1))
    return 1 - (rec_mm + rec_nn + rec_nm)


v = '28 16 17'
pr = probability(*map(int, v.split(' ')))
print(pr)
