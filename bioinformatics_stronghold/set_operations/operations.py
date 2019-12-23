
def from_string(set_string):
    return set(map(int, set_string.strip('{}').split(', ')))


size, set_1, set_2 = open('sets.txt').read().splitlines()
n = int(size)
a, b = from_string(set_1), from_string(set_2)
u = set(range(1, n + 1))

sets = [
    a.union(b),
    a.intersection(b),
    a.difference(b),
    b.difference(a),
    u.difference(a),
    u.difference(b)
]

with open('res.txt', 'w') as res_file:
    res_file.writelines(map(lambda s: f'{str(s)}\n', sets))
