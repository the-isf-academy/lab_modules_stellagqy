# shapes.py
# by Chris Proctor
# Functions which draw fancy shapes

# =============================================================================
# ! Advanced !
# =============================================================================
# This module contains some fancy code that we don't expect you to understand 
# yet. That's ok--as long as we know how to use code, we don't have to 
# understand everything about it. (Do you understand everything about 
# MacOS?) Check out the README for documentation on how to use this code. 

# Of course, if you want to dig into this module, feel free. You can ask a 
# teacher about it if you're interested. 
# =============================================================================

from turtle import *
from math import sin, cos, tau, sqrt

# The gloden ratio
phi = 1.618

def fly(x, y):
    penup()
    goto(x, y)
    pendown()

def nodraw(distance):
    penup()
    forward(distance)
    pendown()

def half_diamond(size, to_the_right=True):
    "Draws two sides of a square, oriented at 45 degrees"
    turn = right if to_the_right else left
    turn(45)
    forward(size/2 * sqrt(2))
    turn(90)
    forward(size/2 * sqrt(2))
    turn(45)

def block_a(height):
    "Starting from the baseline, pointed in the direction of text, draws an A and returns width"
    width = height / phi
    forward(width / 4)
    left(90)
    forward(height / 2)
    half_diamond(width / 2)
    forward(height / 2)
    left(90)
    forward(width / 4)
    left(90)
    forward(height - width/2)
    half_diamond(width, False)
    forward(height - width/2)
    left(90)
    return width

def block_b(height):
    "Starting from the baseline, pointed in the direction of text, draws a B and returns width"
    width = height / phi
    line_width = width / 4
    forward(line_width)
    half_diamond(height / 2, False)
    right(180)
    half_diamond(height / 2, False)
    forward(line_width)
    left(90)
    forward(height)
    left(90)
    return line_width + height / 4

def block_c(height):
    "Starting from the baseline, pointed in the direction of text, draws a B and returns width"
    width = height / phi
    line_width = width / 4
    nodraw(height/2)
    right(180)
    half_diamond(height)
    right(90)
    forward(line_width)
    right(90)
    half_diamond(height - 2 * line_width, False)
    right(90)
    forward(line_width)
    left(90)
    nodraw(-height/2)
    return height/2

def fancy_star(inner_radius, outer_radius, number_of_points):
    "Draws a star with `number_of_points`. Returns the list of points"
    x_origin, y_origin = position()
    points = []
    fly(x_origin, y_origin + inner_radius)
    points.append(position())
    for point in range(number_of_points):
        goto(
            x_origin + inner_radius * sin(tau * (point / number_of_points)), 
            y_origin + inner_radius * cos(tau * (point / number_of_points))
        )
        points.append(position())
        goto(
            x_origin + outer_radius * sin(tau * ((point + 0.5) / number_of_points)), 
            y_origin + outer_radius * cos(tau * ((point + 0.5) / number_of_points))
        )
        points.append(position())
    goto(x_origin, y_origin + inner_radius)
    fly(x_origin, y_origin)
    return points

def square_with_points(size):
    "Like the regular square function, but returns a list of the square's vertices"
    points = []
    for side in range(4):
        points.append(position())
        forward(size)
        right(90)
    return points

def add_perspective(points, origin, depth):
    "Draws a set of points in perspective"
    if isinstance(origin, list):
        origin = tuple(origin)
    original_x, original_y = position()
    original_heading = heading()
    projected_points = []
    for point in points:
        fly(*point)
        setheading(towards(origin))
        forward(depth * distance(origin))
        projected_points.append(position())
    fly(*projected_points[0])
    for point in projected_points:
        goto(*point)
    goto(*projected_points[0])
    fly(original_x, original_y)
    setheading(original_heading)

if __name__ == '__main__':
    from speed import no_delay
    with no_delay():
        for x in range(-200, 200, 50):
            fly(x, 0)
            points = square_with_points(30)
            add_perspective(points, [0, 100], 0.3)
    input("OK")


