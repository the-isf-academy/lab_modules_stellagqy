# fancy_drawing_example.py

from turtle import *
from drawing.shapes import fancy_star
from drawing.movement import no_delay

with no_delay():
    star_size = 200

    for i in range(10):
        if i%5 == 0:
            color('red')
        elif i%5 == 1:
            color('blue')
        elif i%5 == 2:
            color('green')
        elif i%5 == 3:
            color('yellow')
        elif i%5 == 4:
            color('purple')

        begin_fill()
        fancy_star(star_size, star_size + 100, 7)
        end_fill()
        star_size = star_size - 20


hideturtle()
input()
