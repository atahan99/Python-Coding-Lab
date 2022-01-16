"""
Author: Atahan Kucuk
Assignment: 04.5 - Prime List
Date: 10/04/2021

Description:
    This is an application to calculate the prime numbers until the number user inputs


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
   count = int(input('Enter a positive integer: '))
   print(f'The primes up to {count:.0F} are: ',end='')
   #determining the prime numbers
   for n in range(2,count+1):
    #informing the user
    if is_prime(n):
        #determine if there is need for a comma at the end
        if n == count or n == count-1:
            #output without ','
            print(f'{n:.0f}',end='\n')
        else:
            #output with ','
            print(f'{n:.0f},',end=' ')
      
       


if __name__ == '__main__':
    main()
