def find_ins_idx(r, v):
    for i in range(0, len(r)):
        if v < r[i]:
            return i
    return len(r)


def ins_sort(a):
    result = []
    while a:
        value = a.pop(0)  # 리스트에 남은 자료 중 맨 앞의 값을 뽑아냄
        ins_idx = find_ins_idx(result, value)
        result.insert(ins_idx, value)  # 찾은 위치에 값 삽입(이후 값은 한 칸씩 밀려남)

        print(a, result)  # 결과 중간 확인
    return result


d = [2, 4, 5, 1, 3]
print(ins_sort(d))
