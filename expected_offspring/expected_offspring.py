from itertools import product


def dominant(allele_pair):
    return allele_pair[0].isupper() or allele_pair[1].isupper()


def dominant_probability(genotypes):
    return {(m, f): sum(al_a.isupper() or al_b.isupper() for al_a, al_b in product(m, f)) / 4 for m, f in genotypes}


G = [
    ('AA', 'AA'),
    ('AA', 'Aa'),
    ('AA', 'aa'),
    ('Aa', 'Aa'),
    ('Aa', 'aa'),
    ('aa', 'aa'),
]

P = dominant_probability(G)


def expected_offspring(pairs_list):
    return 2 * sum(P[G[i]] * pairs_count for i, pairs_count in enumerate(pairs_list))


input_data = '16141 16279 17527 19305 18609 16608'
pairs_amount = map(int, input_data.split(' '))
offspring = expected_offspring(pairs_amount)
print(offspring)
