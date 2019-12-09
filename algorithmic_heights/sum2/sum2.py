from utils.common import int_list


def find_opposites(a):
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] == -a[j]:
                return i, j
    return -1, -1


_, *lines = open('arrays.txt')
arrays = [int_list(line.rstrip()) for line in lines]

for p, q in map(find_opposites, arrays):
    print(p if p == -1 else f'{p + 1} {q + 1}')
