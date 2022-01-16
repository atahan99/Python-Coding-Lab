"""
Author: Atahan Kucuk
Assignment: 6.3 - vowels
Date: 10/25/2021

Description:
    python app to draw vowels 


"""

from turtle import *


def draw_a():
    """Complete this function to draw the character a."""
    pensize(10)
    left(90)
    forward(80)
    back(40)
    circle(40)
    right(90)
    penup()
    home()


def draw_e():
    """Complete this function to draw the character e."""
    penup()
    left(90)
    forward(40)
    right(90)
    pendown()
    pensize(10)
    back(40)
    forward(80)
    left(90)
    circle(40, 325)
    penup()
    home()


def draw_i():
    """Complete this function to draw the character i."""

    pensize(10)
    left(90)
    forward(80)
    x, y = pos()
    penup()
    goto(x, y+30)
    pendown()
    dot(18)
    penup()
    home()

def draw_o():
    """Complete this function to draw the character o."""
    pensize(10)
    circle(40)
    penup()
    home()


def draw_u():
    """Complete this function to draw the character u."""
    penup()
    left(90)
    forward(80)
    pendown()
    pensize(10)
    right(180)
    forward(40)
    circle(40, 180)
    forward(40)
    back(80)
    right(90)
    penup()
    home()


def start():
    """This function initializes the window and the turtle.
    Do not modify this function.
    """
    setup(600, 400)
    width(9)
    speed(0)
    penup()
    goto(-220, -30)


def main():
    """You can use this for your own testing."""
    pass


if __name__ == '__main__':
    # Do not change this part
    start()
    main()
    done()
