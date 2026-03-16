import turtle

t = turtle.Turtle()
t.speed(0)
t.bgcolor = turtle.Screen().bgcolor  

colors = ["red", "orange", "gold", "green", "blue", "purple"]
size = 2

for i in range(300):
    t.pencolor(colors[i % 6])
    t.forward(size)
    t.right(91.4)         # golden angle approximation
    size += 1.2

turtle.done()