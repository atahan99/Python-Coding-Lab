"""
Author: Atahan Kucuk
Assignment: 08.4 - Number Writer
Date: 11/15/2021

Description:
    This is an application that gets user input for the amount of numbers to be generated and dumbs the created random numbers into a text file. 


"""

import random 

def Rand(num): # function to generate random numbers
   f=open("random_numbers.txt","a") # opens file
   res = [] # array to store the generated random numbers
   for j in range(num):      
       res.append(random.randint(1019, 1215))
   # travese over the list
   for j in res:
       f.write(str(j)) # writes into file
       f.write("\n")
   f.close()
   return res # returns resultant random numbers list

def main():

    
    # user input to g
    n=int(input("How many numbers would you like? "))
    Rand(n)


if __name__ == '__main__':
    main()
