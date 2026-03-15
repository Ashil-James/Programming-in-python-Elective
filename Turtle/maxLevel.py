import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(800, 800)

t = turtle.Turtle()
t.speed(1)       

# Sun
t.color("yellow")
t.penup(); t.goto(0, -30); t.pendown()
t.begin_fill(); t.circle(30); t.end_fill()

# Orbits and planets
planets = [
    (80,  "skyblue",  8,  "Earth"),
    (130, "red",      6,  "Mars"),
    (180, "orange",   14, "Jupiter"),
]

for orbit_r, color, planet_r, name in planets:
    # Draw orbit ring
    t.color("gray")
    t.penup(); t.goto(0, -orbit_r); t.pendown()
    t.circle(orbit_r)

    # Draw planet
    t.color(color)
    t.penup(); t.goto(orbit_r, 0); t.pendown()
    t.begin_fill(); t.circle(planet_r); t.end_fill()

    # Label
    t.penup(); t.goto(orbit_r + planet_r + 5, 0)
    t.write(name, font=("Arial", 9, "normal"))

screen.mainloop()