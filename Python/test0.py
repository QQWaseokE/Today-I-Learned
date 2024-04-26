def fine_min_dix(a):
    n = len(a)
    min_idx = 0
    for i in range(1, n):
        if a[i] < a[min_idx]:
            min_idx = i
    return min_idx


def sel_sort(a):
    result = []
    while a:
        min_idx = fine_min_dix(a)
        value = a.pop(min_idx)
        result.append(value)
    return result


d = [2, 4, 5, 1, 3]
print(sel_sort(d))
