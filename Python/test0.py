def sum_n(n):
    sum = n * (n + 1) / 2

    return sum


print(sum_n(10))


def sum_n2(n):
    sum = 0
    for x in range(1, n + 1):
        sum = sum + x
    return sum


print(sum_n2(10))
