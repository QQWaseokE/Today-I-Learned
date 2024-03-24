import random
import turtle as t

t.shape("turtle")
t.speed(0)

for x in range(500):
    a = random.randint(1, 360)
    t.right(a)
    t.fd(50)
