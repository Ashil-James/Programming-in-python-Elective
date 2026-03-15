import turtle

def draw_rectangle(t, width, height):
    """Draw a rectangle with the given width and height.

    t: Turtle
    width: width of the rectangle
    height: height of the rectangle
    """
    for i in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
        
def draw_square(t, size):

    for i in range(4):
        t.forward(size)
        t.right(90)
        
def draw_triangle(t, size):
    
    for i in range(3):
        t.forward(size)
        t.left(120)
        
def draw_circle(t, radius):
    t.circle(radius) # Draw a circle with the given radius using inbuild function

def circle_manual(t):
    for i in range(360):
        t.forward(1)   # draw a tiny 1px line
        t.right(1)     # turn right by 1 degree

t = turtle.Turtle()
circle_manual(t)
turtle.done()