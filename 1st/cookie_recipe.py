"""
Author: Atahan Kucuk
Assignment: 01.3 - Cookie Recipe
Date: 09/13/2021

Description:

    simple application to determine the amount of ingredients needed to make given number Cookies
"""


def main():

    #asking the user for the amount of cookies they want to make
    Cookies=int(input('How many cookies do you want to make? '))
    #calculating the required ingredients
    Sugar = format(float((1.75 / 48 ) * Cookies),'7.2f')
    Butter = format(float((1 / 48)* Cookies),'7.2f')
    Flour = format(float((2.5 / 48 )* Cookies),'7.2f')
    #displaying the ingredients
    print('To make', Cookies ,'cookies, you will need: ')
    print(Sugar,'cups of sugar')
    print(Butter,'cups of butter')
    print(Flour,'cups of flour')



if __name__ == '__main__':
    main()
