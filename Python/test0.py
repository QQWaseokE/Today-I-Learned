import random
import time

w = ["cat", "dog", "fox", "monkey", "mouse", "panda", "frog", "snake", "wolf"]
n = 1
print("[타자게임] 준비되면 엔터!")
input()
start = time.time()

q = random.choice(w)
while n <= 5:
    print("문제", n)
    print(q)
    x = input()
    if q == x:
        print("PASS!")
        n = n + 1
        q = random.choice(w)
    else:
        print("Wrong! Again!")

end = time.time()
result = end - start
result = format(result, ".2f")
print("TIME:", result, "초")
