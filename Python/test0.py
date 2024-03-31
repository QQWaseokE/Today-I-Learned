def fact(a):
    if a == 1:
        return 1
    if a == 0:
        return 0
    return fact(a - 1) + fact(a - 2)


print(fact(10))
