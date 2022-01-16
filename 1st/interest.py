"""
Author: Atahan Kucuk
Assignment: 01.2 - interest
Date: 09/13/2021

Description:
    This is a simple app to calculate the future value of users bank account
    based on the user input such as number of years, initial deposit, interest rate
    and number of times it has been compounded

"""


def main():

    #asking user for input data
    print('Please enter the following quantities.')
    P=float(input('  How much is the initial deposit? '))
    r=(float(input('  What is the annual interest rate in percent? ')))/100
    n=float(input('  How many times per year is the interest compounded? '))
    t=float(input('  How many years will the account earn interest? '))
    #calulating the future value
    FV = format((P*(1+r/n)**(n*t)), '10,.2f')
    #informing the user about their accounts future value
    print('\nAt the end of ',t,' years, this account will be worth $',FV,'.')


if __name__ == '__main__':
    main()
