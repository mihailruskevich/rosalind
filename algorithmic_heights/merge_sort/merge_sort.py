from utils.arrays import merge
from utils.common import int_list


def merge_sort(a):
    queue = [[v] for v in a]
    while len(queue) > 1:
        queue.append(merge(queue.pop(0), queue.pop(0)))
    return queue[0]


_, line = open('array.txt')
arr = int_list(line)
sorted_arr = merge_sort(arr)

open('sorted_array.txt', 'w') \
    .write(' '.join(map(str, sorted_arr)))
