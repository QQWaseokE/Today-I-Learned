def find_min(a):
    n = len(a)
    min = a[0]

    for x in range(1, n):
        if min > a[x]:
            min = a[x]
    return min


v = [17, 92, 18, 33, 58, 7, 33, 42]
print(find_min(v))
