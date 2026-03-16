import turtle 


screen = turtle.Screen()
screen.title("Flower")
screen.bgcolor("white")
screen.setup(600, 600)

t= turtle.Turtle()

t.circle(80,60)
t.left(120)
t.circle(80,60)
t.left(120)
t.left(60)
t.circle(80,60)

screen.mainloop()