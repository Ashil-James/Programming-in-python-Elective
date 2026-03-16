import turtle

t = turtle.Turtle()
t.speed(0)

size = 1

for i in range(400):
    t.forward(size)
    t.right(10)          # small angle → smooth curve
    size += 0.5          # grow slowly → tight spiral

turtle.done()

"""
import turtle

t = turtle.Turtle()
t.speed(0)

size = 5
for i in range(100):
    t.forward(size)
    t.right(90)       # square turn
    size += 3         # grow each step

turtle.done()
"""