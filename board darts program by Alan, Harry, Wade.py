import turtle
import random 

w = turtle.Screen()

t = turtle.Turtle()
t.speed(10)
t.hideturtle()
t.fillcolor('blue')
t.begin_fill()
t.forward(200)
t.right(90)
t.forward(200)
t.right(90)
t.forward(200)
t.right(90)
t.forward(200)
t.end_fill()

t.penup()
t.right(180)
t.forward(50)
t.left(90)
t.forward(50)
t.pendown()
t.fillcolor('red')
t.begin_fill()
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.end_fill()

n = int(input("how many times would you darts you want to throw: "))
t.color('yellow')
cnt = 0
t.speed(15)
for i in range(n):
  a = random.uniform(0, 1)
  a = round(a, 2)
  b = random.uniform(0, 1)
  b = round(b, 2)
  t.penup()
  t.goto(a * 200, -b * 200)
  t.pendown()
  t.circle(1)
  if(a * 200 <= 150 and a * 200 >= 50 and b * 200 <= 150 and b * 200 >= 50):
    cnt += 1
ans = float(cnt/n)
print("{} out of {} times of darts were thrown within the inner rectangle".format(cnt, n))
print("{} percent of darts were thrown in the inner square".format(ans*100))
  
