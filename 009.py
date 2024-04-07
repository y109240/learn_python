# https://docs.python.org/3/library/turtle.html
# 거북이 그래픽

import turtle
t = turtle.Turtle()

t.speed("fast")
t.shape("turtle")
t.turtlesize(2)
t.color("green")
t.pencolor("green")
t.screen.bgcolor("light gray")

# 예제
for steps in range(100):
    for c in ("red", "orange", "yellow", "green", "blue", "purple"):
        t.color(c)
        t.forward(steps)
        t.right(30)

# 별 그려보기
t.forward(100)
for i in range(5):
  t.right(144)
  t.forward(200)
t.setpos(0, 0)

# turtle star?
for i in range(36):
  t.forward(240)
  t.right(170)

for j in range(10):
  for i in range(5):
    t.forward(100)
    t.right(144)
  t.left(36)


# 이런것도 할수있다 - 장미그리기
t.speed(50)
t.bgcolor("black")
t.color("pink")
t.setup(650, 900)
# 꽃 그리기
for i in range(1, 201):
    t.pensize(1/50)
    t.forward(i)
    t.left(65)
# 줄기 그리기
t.color("lightblue")
t.setheading(270)
for i in range(50):
    t.pensize(25-i/2)
    t.forward(i/4)
# 잎 그리기
t.color("yellowgreen")
t.setheading(60)
for x in range(100):
    t.pensize(100-x)
    t.forward(x/10)
t.ht()

turtle.done()
