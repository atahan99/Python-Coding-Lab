"""
Author: Atahan Kucuk
Assignment: 03.2 - Sum Average
Date: 09/13/2021

Description:
    It is a simple application to calculate the total and average of the input numbers that the user gave.


"""


def main():

    #Declaring the variables
    msg = 'Enter a non-negative number (negative to quit): '
    count, total, average = 0 , 0 ,0
    number = float(input(msg))
    #Getting the user input & calculating the count and total 
    while number >= 0: 
        count+=1
        total+=number
        number = float(input(msg))
    #Calculating the average and informing the user 
    if count >0 :
        average = float(total/count)
        print(f'  You entered {count:.0f} numbers.')
        print(f'  Their sum is {total:.3f} and their average is {average:.3f}.')
    else:
        print("  You didn't enter any numbers.")




if __name__ == '__main__':
    main()
