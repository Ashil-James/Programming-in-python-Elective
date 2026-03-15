import turtle

screen = turtle.Screen()
t = turtle.Turtle()

def move_forward():  t.forward(30)
def turn_left():     t.left(30)
def turn_right():    t.right(30)
def clear_screen():  t.clear(); t.home()

screen.listen()
screen.onkey(move_forward,  "Up")
screen.onkey(turn_left,     "Left")
screen.onkey(turn_right,    "Right")
screen.onkey(clear_screen,  "c")

screen.mainloop()