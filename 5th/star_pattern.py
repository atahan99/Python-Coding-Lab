"""
Author: Atahan Kucuk
Assignment: 5.3 - Star Pattern
Date: 10/11/2021

Description:
    It is an application to draw star patterns given the user input 


"""

from turtle import *

def start():
    """This function initializes the window and the turtle.
    Do not modify this function.
    """
    setup(564, 564)
    width(7)
    side_length = 60 # Also the radius of a circle enclosed by the star.
    penup()
    goto(0, -side_length) # Start at the bottom of the star.
    pendown()

def main():
    """Write your code below this line."""
    
    #asking user for input points to be used
    points = int(input('How many points would you like on the star: '))
    #defining the pen size for the perimeter
    pensize(5)
    pencolor('black')
    #defining the angels
    a = float(360/points)
    b = 2*a
    #loop to draw the star
    fillcolor('pink')
    begin_fill()
    left((180-b)/2)
    for i in range(points):
        forward(60)
        left(180 - b)
        forward(60)
        right(180 - a)
    end_fill()
    



# Do not change anything after this line.
if __name__ == '__main__':
    start()
    main()
    done()
