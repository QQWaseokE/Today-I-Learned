import turtle as t

n = 50
t.bgcolor("black")
t.color("green")
t.speed(10)

for x in range(n):
    t.circle(80)
    t.lt(360 / n)
