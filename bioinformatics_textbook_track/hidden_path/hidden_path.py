from functools import reduce


# T = {
#     ('A', 'x'): 0.612,
#     ('A', 'y'): 0.314,
#     ('A', 'z'): 0.074,
#     ('B', 'x'): 0.346,
#     ('B', 'y'): 0.317,
#     ('B', 'z'): 0.336
# }

def create_matrix(table_data):
    values, *pr_lines = table_data
    res_map = {}
    for pr_line in pr_lines:
        key = pr_line[0]
        for i, pr in enumerate(pr_line[1:]):
            res_map[(key, values[i])] = float(pr)
    return res_map


def probability(x, p, p_matrix):
    return reduce(lambda res, pair: res * p_matrix[pair], zip(p, x), 1)


with open('data.txt') as file:
    lines = [line.rstrip() for line in file.readlines()]
    value, path = lines[0], lines[4]
    table = [line.split() for line in lines[8:]]
    probability_matrix = create_matrix(table)
    result = probability(value, path, probability_matrix)
    print(result)
