"""
Author: Atahan Kucuk
Assignment: 6.4 - Arch Spiral
Date: MM/DD/YYYY

Description:
    This is an application to draw arch spiaral using python turtle module


"""

from turtle import *

# Import additional modules below this line.
import math

def start():
    """This function initializes the window and the turtle.
    Do not modify this function.
    """
    setup(564, 564)
    width('5')


def main():
    """Write your mainline logic here."""
    

    for i in range(0,2161):
        #calculating the radian
        rad = i*math.pi/180
        #calculating the angles
        x = (i/math.pi**2)*math.cos(rad)
        y = (i/math.pi**2)*math.sin(rad)
        setpos(x,y)



if __name__ == '__main__':
    # Do not change this part
    start()
    main()
    done()
