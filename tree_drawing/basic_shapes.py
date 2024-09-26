# shapes.py

from turtle import color, begin_fill, end_fill, forward, right, left

def triangle(size,triangle_color):
    # draws a triangle of any size and color

    color(triangle_color)
    begin_fill()
    for i in range(3):
        forward(size)
        left(120)
    end_fill()


def rectangle(width, height, rectangle_color):
    # draws a rectangle of any size and color

    color(rectangle_color)
    begin_fill()
    for i in range(2):
        forward(width)
        right(90)
        forward(height)
        right(90)
    end_fill()