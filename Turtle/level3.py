import turtle 


screen = turtle.Screen()
screen.title("Flower")
screen.bgcolor("white")
screen.setup(600, 600)

t= turtle.Turtle()
t.speed(0)
#t.hideturtle()

#draw one petal
def draw_petal(color):
    t.color("darkgreen", color)
    t.begin_fill()
    t.circle(80,60)
    t.left(120)
    t.circle(80,60)
    t.left(120)
    t.end_fill()
    
colors = ["red", "orange", "yellow", "green", "blue", "violet"]
for i in range(6):
    draw_petal(colors[i])
    t.left(60)
    
#Draw Stem
t.penup()
t.goto(0, 0)
t.pendown()
t.color("green")
t.pensize(4)
t.setheading(270)
t.forward(150)

t.penup()
t.goto(0,-60)
t.pendown()
t.setheading(180)
t.color("darkgreen","green")
t.begin_fill()
t.circle(40, 90)
t.left(90)
t.circle(40, 90)
t.end_fill()

t.penup()
t.goto(0, -100)
t.pendown()
t.setheading(0)
t.begin_fill()
t.circle(40, 90)
t.left(90)
t.circle(40, 90)
t.end_fill()

t.penup()
t.goto(0, 0)
t.pendown()
t.pensize(1)
t.color("black")
t.begin_fill()
t.circle(10)
t.end_fill()

screen.mainloop()