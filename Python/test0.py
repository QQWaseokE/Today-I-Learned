import time
import random


def max_profit_slow(prices):
    n = len(prices)
    max_profit = 0

    for i in range(0, n - 1):
        for j in range(i + 1, n):
            profit = prices[j] - prices[i]
            if profit > max_profit:
                max_profit = profit
    return max_profit


def max_profit_fast(prices):
    n = len(prices)
    max_profit = 0
    min_price = prices[0]

    for i in range(1, n):
        profit = prices[i] - min_price
        if profit > max_profit:
            max_profit = profit
        if prices[i] < min_price:
            min_price = prices[i]
    return max_profit


def test(n):  # n = 주가 개수
    a = []
    for i in range(0, n):
        a.append(random.randint(5000, 20000))  # 주가로 사용

    # 느린 O(n*n) 알고리즘 테스트
    start = time.time()
    mps = max_profit_slow(a)
    end = time.time()
    time_slow = end - start

    # 빠른 O(n) 알고리즘 테스트
    start = time.time()
    mpf = max_profit_fast(a)
    end = time.time()
    time_fast = end - start

    # 결과 출력 : 계산 결과 (mps와 mpf가 같아야 함)
    print(n, mps, mpf)

    # 결과 출력 : 계산 시간 비교
    m = 0
    if time_fast > 0:
        m = time_slow / time_fast

    print("%d %.5f %.5f %.2f" % (n, time_slow, time_fast, m))


test(100)
test(10000)
test(100000)
