from utils.common import int_list


def insertion_sort(a):
    swap_count = 0
    for i in range(2, len(a)):
        j = i
        while j > 0 and a[j] < a[j - 1]:
            a[j - 1], a[j] = a[j], a[j - 1]
            j -= 1
        swap_count += i - j
    return swap_count


arr = int_list(next(open('array.txt')))
swaps = insertion_sort(arr)
print(swaps)
