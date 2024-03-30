def fact(a):
    if a <= 0:
        return v[0]
    return max(v[a], fact(a - 1))


v = [103, 92, 18, 33, 100, 7, 33, 42]
n = len(v)
r = n - 1
print(fact(r))
