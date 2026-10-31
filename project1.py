import turtle

# Set up screen
screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.title("COMP115 Project 1")

t = turtle.Turtle()
t.speed(0)

# Function to draw a filled rectangle/square
def draw_rectangle(width, height, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

# Function to draw a triangle (for roof)
def draw_triangle(size, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.left(120)
    t.end_fill()

# 1. Draw Grass
t.penup()
t.goto(-400, -300)
t.pendown()
draw_rectangle(800, 250, "forestgreen")

# 2. Draw Sun
t.penup()
t.goto(-250, 180)
t.pendown()
t.fillcolor("yellow")
t.begin_fill()
t.circle(40)
t.end_fill()

# 3. Draw House Base
t.penup()
t.goto(-70, -150)
t.pendown()
draw_rectangle(140, 150, "royalblue")

# 4. Draw Roof
t.penup()
t.goto(-90, 0)
t.pendown()
draw_triangle(180, "darkblue")

# 5. Draw Door
t.penup()
t.goto(-20, -150)
t.pendown()
draw_rectangle(40, 60, "saddlebrown")

# 6. Draw Windows (using a loop)
for x_pos in [-50, 20]:
    t.penup()
    t.goto(x_pos, -60)
    t.pendown()
    draw_rectangle(30, 40, "white")

t.hideturtle()
turtle.done()