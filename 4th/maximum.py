"""
Author: Atahan Kucuk
Assignment: 04.2 - Maximum
Date: 10/04/2021

Description:
    It is a simple application to find the maximum of 2 integers given the user input


"""
#finding the max
def max_of_two(first,second):
    if first > second :
        return first
    else : 
        return second


def main():
    #asking user for integers
    first = int(input('Enter the first integer: '))
    second = int(input('Enter the second integer: '))
    #informing the user for the output
    print(f'The number {max_of_two(first,second):.0f} is greater.')
    
 



if __name__ == '__main__':
    main()
