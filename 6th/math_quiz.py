"""
Author: Atahan Kucuk
Assignment: 06.1 - Math Quiz
Date: 10/18/2021

Description:
    it is an simple application that generates random numners and asks the user for the sum.


"""
import random as r

def random_number( x):
   # generate x digit number
   num = r.randint(10**(x-1),(10**x)-1)
   return num
    
def main():
    # generating random numbers
    two = random_number(2)
    three= random_number(3)
    #display the calculation
    print(f'{two:5.0f}')
    print(f'+ {three:.0f}')
    print('-----')
    total = two+three
    #ask user for result
    calc = int(input('= '))
    #check the result
    if calc == total:
        print('Correct -- Good Work!')
    else:
        print(f'Incorrect. The correct answer is {total:.0f}.')



if __name__ == '__main__':
    main()
