# 리스트에서 특정 숫자의 위치 찾기
# 입력 ; 리스트 a, 찾는 값 x
# 출력 : 찾으면 그 값의 위치, 찾지 못하면 -1


def search_list(a, x):
    list = []
    n = len(a)
    for i in range(0, n):
        if x == a[i]:
            list.append(i)

    return list


v = [17, 92, 18, 33, 58, 7, 33, 42]
print(search_list(v, 18))
print(search_list(v, 33))
print(search_list(v, 900))
