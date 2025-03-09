# program to generate an optical illusion of a 3d sphere using turtle graphics

import turtle

# function to draw a single circle at a given position
def draw_circle(t, radius, color, x, y):
    t.penup()
    t.goto(x, y - radius)  # adjust starting point to the bottom of the circle
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# function to create the sphere illusion
def create_sphere_illusion(t):
    # define shades/colors to simulate lighting (darker to lighter)
    colors = ["black", "dimgray", "gray", "darkgray", "lightgray", "gainsboro"]
    
    # circle sizes (larger to smaller to create 3d illusion)
    radii = [120, 100, 80, 60, 40, 20]

    # loop to draw concentric circles from largest to smallest
    for radius, color in zip(radii, colors):
        draw_circle(t, radius, color, 0, 0)

# main function setup
if __name__ == "__main__":
    # setup turtle screen
    window = turtle.Screen()
    window.bgcolor("white")

    # create turtle object
    pen = turtle.Turtle()
    pen.speed(0)  # maximum drawing speed

    # generate the sphere illusion
    create_sphere_illusion(pen)

    # exit on click
    window.exitonclick()