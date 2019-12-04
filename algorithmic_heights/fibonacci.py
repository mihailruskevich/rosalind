
def f(n):
    a, b = 0, 1
    for _ in range(n):
        c = a + b
        a, b = b, c
    return a


result = f(21)
print(result)
