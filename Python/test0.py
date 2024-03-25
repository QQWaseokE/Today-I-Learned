def sum_fun(n):
    s = 1
    for x in range(1, n + 1):
        s = s * x
    return s


print(sum_fun(5))
print(sum_fun(10))
