def search_list(a, b, x):
    n = len(a)
    for i in range(0, n):
        if x == a[i]:
            return stu_name[i]

    return "?"


stu_no = [39, 14, 67, 105]
stu_name = ["Justin", "John", "Mike", "Summer"]

print(search_list(stu_no, stu_name, 39))
print(search_list(stu_no, stu_name, 67))
print(search_list(stu_no, stu_name, 100))
