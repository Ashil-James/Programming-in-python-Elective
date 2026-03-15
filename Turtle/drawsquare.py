import turtle

def draw_square(t, size):
    """Draw a square with sides of the given size.

    t: Turtle
    size: length of the sides of the square
    """
    for i in range(4):
        t.forward(size)
        t.right(90)


t = turtle.Turtle()
draw_square(t, 100)
turtle.done()