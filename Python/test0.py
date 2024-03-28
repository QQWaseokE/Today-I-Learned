def sum_n(n):
    sum = 0
    for x in range(1, n + 1):
        sum = sum + x * x
    return sum


print(sum_n(10))
