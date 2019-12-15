from utils.arrays import partition, equality_partition
from utils.common import int_list


def three_way_partition(a, x):
    i = partition(a, x, 0, len(a) - 1)
    equality_partition(a, x, i, len(a) - 1)


_, line = open('array.txt')
arr = int_list(line)

three_way_partition(arr, arr[0])
res = ' '.join(map(str, arr))
open('res.txt', 'w').write(res)
