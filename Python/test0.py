def fact(a):
    if a <= 1:
        return a
    return fact(a - 2) + fact(a - 1)


print(fact(10))
