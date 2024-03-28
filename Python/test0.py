def connect_friend(a):
    n = len(a)

    for i in range(0, n - 1):
        for j in range(i + 1, n):
            print(a[i], "-", a[j])


name = ["Tom", "Jerry", "Mike"]
print(connect_friend(name))
print()
name2 = ["Tom", "Jerry", "Mike", "John"]
print(connect_friend(name2))
