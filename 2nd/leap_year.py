"""
Author: Atahan Kucuk
Assignment: 02.1 - Leap Year
Date: 09/18/2021

Description:
    This application is a simple applciation to figure out how many days does February has in a given year. It uses calculations to figure out if the year is a leap year.


"""


def main():

    #Declaraation of variables
    div100 = False
    div400 = False
    div4 = False
    leap = False 
    year = int(input('Please input a year: '))
    day = 28
    
    # Deciding if the year is a leap year or not 
    if ( year % 100) == 0:
        div100 = True
    if ( year % 400) == 0:
        div400 = True
    if ( year % 4 ) == 0:
        div4 = True
    if div100 == True and div400 == True:
        leap = True
    if div100 == False and div4 == True:
        leap = True
    if leap == True:
        day = 29
    # Displaying the output 
    print (f'In the year { year:.0f}, February has {day:.0f} days.' )
    
    

if __name__ == '__main__':
    main()
