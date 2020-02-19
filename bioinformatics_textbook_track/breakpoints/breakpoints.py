
def parse(p):
    return list(map(int, p[1:-1].split()))


def count_breakpoints(a):
    x = [0, *a, len(a) + 1]
    return sum(1 for p in zip(x, x[1:]) if p[1] - p[0] != 1)


with open('array.txt') as [line]:
    arr = parse(line)
    res = count_breakpoints(arr)
    print(res)
