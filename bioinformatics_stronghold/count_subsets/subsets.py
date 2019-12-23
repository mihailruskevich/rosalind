
def subsets_count(n):
    return 2 ** n


set_length = 3
res = subsets_count(set_length) % 1000000
print(res)
