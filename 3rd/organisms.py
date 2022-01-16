"""
Author: Atahan Kucuk
Assignment: 03.4 - Organisms
Date: 09/24/2021

Description:
   This application takes user input and uses that in order to predict the approximate size of a population of organisims


"""


def main():
    #Declaring variables and asking user input 
    number = float(input('Starting number, in million: '))
    increase = float(input('Average daily increase, in percent: ')) / 100.0
    days= int(input('Number of days to multiply: '))
    population = 0

    print('Day   Approx. Pop')
    #Caculating the population
    for i in range(0,days+1):
        population=number*(1+increase)**(i)
        #Informing the user of the results
        print(f'{i:3.0f}      {population:8.4f}')



if __name__ == '__main__':
    main()
