"""
Author: Atahan Kucuk
Assignment: 04.4 - Prime Numbers
Date: 10/04/2021

Description:
    This is an application to determine if the numbers are prime or not


"""
#deteriming if the number is prime
def is_prime(number):

    if number ==2 or number ==3:
        return True
    if number%2 == 0 or number < 2 : 
        return False
    for i in range(3,int(number**(1/2)+1),2):
        if number%i == 0 :
            return False
    return True


def main():

    #asking user for input
    msg = 'Enter a positive integer (-1 to quit): '
    number = 0
    prime = False
    
    #running the loop until user quits the loop
    while number >= -1 : 
        number = int(input(msg))
        if number == -1:
            break
        prime = is_prime(number)
        #informing the user if the number is prime
        if prime == True :
            print(f'  {number:.0f} is prime!')
        else:
            print(f'  {number:.0f} is not prime.')


if __name__ == '__main__':
    main()
