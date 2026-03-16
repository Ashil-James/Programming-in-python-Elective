import turtle

screen = turtle.Screen()
t = turtle.Turtle()

def draw_octagon(t, size):
    t.color("blue","green")
    t.begin_fill()
    for i in range(8):
        t.forward(size)
        t.left(45)
    t.end_fill()
        
        
draw_octagon(t, 100)
screen.mainloop()