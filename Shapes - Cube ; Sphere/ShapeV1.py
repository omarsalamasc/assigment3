# import turtle library for drawing
import turtle

# function to draw a single square at (x,y) location
def draw_square(t, size, color, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.left(90)
    t.end_fill()

# function to create the optical illusion
def create_illusion(t):
    colors = ["black", "gray", "lightgray"]
    size = 100  # square size

    # position coordinates for squares to create cube illusion
    positions = [
        (0, 0, colors[0]),
        (30, 30, colors[1]),
        (-30, 30, colors[2])
    ]

    # draw squares to simulate cube faces
    for x, y, color in positions:
        draw_square(t, size, color, x, y)

# main function to set up window and start drawing
if __name__ == "__main__":
    # set up the drawing window
    window = turtle.Screen()
    window.bgcolor("white")

    # creating a single turtle object
    pen = turtle.Turtle()
    pen.speed(0)  # fastest drawing speed

    # call function to create optical illusion
    create_illusion(pen)

    # finish drawing
    window.exitonclick()