from utils.common import int_list


def major(a):
    if len(a) > 2:
        half = len(a) // 2
        x, y = major(a[:half]), major(a[half:])
        if x == -1 and y == -1:
            return -1
        else:
            m = x if x != -1 else y
            return m if a.count(m) > half else -1
    else:
        return a[0] if len(set(a)) == 1 else -1


with open('arrays.txt') as (_, *lines):
    arrays = [int_list(line.rstrip()) for line in lines]
    major_elements = [major(arr) for arr in arrays]
    print(*major_elements)
