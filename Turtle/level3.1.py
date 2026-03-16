import turtle

# ── Setup ──────────────────────────────────────────
screen = turtle.Screen()
screen.title("Circle at (100, 100)")
screen.bgcolor("white")
screen.setup(600, 600)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

cx, cy = 100, 100
radius = 80

t.penup()
t.goto(cx, cy - radius)
t.pendown()
# ── Draw Circle Manually ──────────────────────────
t.color("blue","lightblue")
t.begin_fill()
t.circle(radius)
t.end_fill()

screen.mainloop()