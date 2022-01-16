"""
Author: Atahan Kucuk
Assignment: 02.2 - Software Sales
Date: 09/18/2021

Description:
   This application is used to calculate the total sale price of a software. Calcualtion includes the conditions for different discount ranges and informs the user for the totla discount applied. 


"""


def main():

    #Declaring variables
    quantity = int(input('How many packages will be purchased: '))
    discount = 0
    #Testing the conditions
    if quantity < 0 : 
        print('  Invalid Input!')
        quit()
    if quantity > 0 and quantity <= 4 :
        print('  No discount Applied.')
        discount = 1
    if quantity >= 5 and quantity <= 24 : 
        print('  10% discount applied.')
        discount = 0.9
    if quantity >= 25 and quantity <= 49 :
        print('  20% discount applied.')
        discount = 0.8
    if quantity >= 50 and quantity <= 99 : 
        print('  30% discount applied.')
        discount = 0.7
    if quantity >= 100 : 
        print('  45% discount applied.')
        discount = 0.55
    #Calcualting the the total 
    total = float((79*quantity*discount))
    print(f'  The total price for purchasing {quantity:.0f} packages is ${total:,.2f}.')
    

    
 



if __name__ == '__main__':
    main()
