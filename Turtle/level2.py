import turtle

def fill_square(t, size):
    t.color("blue", "yellow")  # Set pen color to blue and fill color to yellow
    t.begin_fill()  # Start filling the shape
    for i in range(4):
        t.forward(size)
        t.right(90)
    t.end_fill()  # Finish filling the shape
    
def spiral(t, size):
    for i in range(50):
        t.forward(size)
        t.right(100)
        size += 5
def rosette_pattern(t, petals):
    colors = ["red", "orange", "yellow", "green", "blue", "violet"]
    for i in range(petals):
        t.color(colors[i % len(colors)])  # Cycle through colors
        t.circle(80)
        t.right(10)
        
def star(t, size):
    for _ in range(5):
        t.forward(size)
        t.right(144)

def fractal_star(t, size):
    for i in range(12):
        star(t, size)
        t.right(30)

     
t = turtle.Turtle()
spiral(t, 100)
turtle.done()